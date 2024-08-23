# Assuming the necessary data is imported at the top
from npc_data_refactored import archestats, atbmods, perception, armorclass, hp, weapons, weapondamage, skills_refactored, skillmodifiers, archweapon_groups, savingthrows
# Spell Options
from npc_data_refactored import fullcaster_spellslots, halfcaster_spellslots, partialcaster_spellslots, spell_list, spell_stats
# Archetype ATF Options
from npc_data_refactored import atfpointbuy, archer_atfoptions,bard_atfoptions,berserker_atfoptions,cleric_atfoptions,occultist_atfoptions, paladin_atfoptions, pugilist_atfoptions, shaman_atfoptions, soldier_atfoptions, sorcerer_atfoptions,thief_atfoptions,wanderer_atfoptions,wizard_atfoptions,universal_atfoptions,rare_atfoptions
import random
import re

# Function to extract numerical value from the damage string
def extract_damage_value(damage_string):
    match = re.search(r'\((\d+)\)', damage_string)
    if match:
        return int(match.group(1))
    else:
        return 0

# Function to randomly select spells
def select_spells(archetype, level):
    archetype_capitalized = archetype.capitalize()
    spell_casting_type = archestats['spell_cast'][archestats['Archetype'].index(archetype_capitalized)]
    spell_school1 = archestats['spell_school1'][archestats['Archetype'].index(archetype_capitalized)]
    spell_school2 = archestats['spell_school2'][archestats['Archetype'].index(archetype_capitalized)]

    if spell_casting_type == 'full':
        spell_slots = fullcaster_spellslots
    elif spell_casting_type == 'half':
        spell_slots = halfcaster_spellslots
    elif spell_casting_type == 'partial':
        spell_slots = partialcaster_spellslots
    else:
        return [], None, None

    spells_selected = []
    used_school = None

    # Include rank 0 spells (cantrips)
    for rank in range(0, level + 1):
        rank_key = f'rank{rank}_total'
        if rank_key not in spell_slots or level - 1 >= len(spell_slots[rank_key]):
            continue

        spell_count = spell_slots[rank_key][level - 1]

        # Handle 'none' for spell_school1
        if spell_school1 == 'none' and used_school is None:
            available_schools = set(spell_list.get(f'rank_{rank}_school', []))
            available_schools.discard('none')
            if available_schools:
                used_school = random.choice(list(available_schools))
            else:
                continue

        if used_school:
            rank_spells = [
                (rank, spell) for i, spell in enumerate(spell_list.get(f'rank_{rank}', [])) 
                if i < len(spell_list.get(f'rank_{rank}_school', [])) and spell_list[f'rank_{rank}_school'][i] == used_school
            ]
        else:
            rank_spells = [
                (rank, spell) for i, spell in enumerate(spell_list.get(f'rank_{rank}', [])) 
                if i < len(spell_list.get(f'rank_{rank}_school', [])) and spell_list[f'rank_{rank}_school'][i] == spell_school1
            ]

        random.shuffle(rank_spells)
        spells_selected += rank_spells[:min(2, spell_count)]
        spell_count -= min(2, len(rank_spells))

        # Select spells from spell_school2 if needed and available
        if spell_count > 0 and spell_school2 != 'none' and spell_school2 != '0':
            rank_spells = [
                (rank, spell) for i, spell in enumerate(spell_list.get(f'rank_{rank}', [])) 
                if i < len(spell_list.get(f'rank_{rank}_school', [])) and spell_list[f'rank_{rank}_school'][i] == spell_school2
            ]
            random.shuffle(rank_spells)
            spells_selected += rank_spells[:spell_count]

        # If no specific school is defined, pull randomly
        if spell_count > 0 and (spell_school1 == 'none' or spell_school2 == 'none'):
            rank_spells = [(rank, spell) for spell in spell_list.get(f'rank_{rank}', [])]
            random.shuffle(rank_spells)
            spells_selected += rank_spells[:spell_count]

    return spells_selected, used_school, spell_school2


def select_talents(archetype, level, include_universal, include_rare):
    # Normalize the archetype name to match the case in archetype_atfoptions
    archetype_lower = archetype.lower()
    talent_data = globals().get(f"{archetype_lower}_atfoptions")
    
    if not talent_data:
        return []

    # Get available points based on the level
    available_points = atfpointbuy['atf_points'][level - 1]
    
    # List of selected talents
    selected_talents = []

    # Keep track of remaining points
    remaining_points = available_points

    # Randomly shuffle archetype-specific talents to simulate random selection
    archetype_talents = list(zip(talent_data['atf_name'], talent_data['atf_info'], talent_data['atf_cost']))
    random.shuffle(archetype_talents)

    # Ensure at least one archetype talent is selected first
    for name, info, cost in archetype_talents:
        if remaining_points >= cost:
            selected_talents.append((name, info))
            remaining_points -= cost
            break  # Only select the first archetype talent and exit this loop

    # If no points left after selecting the first archetype talent, return the selected talents
    if remaining_points == 0:
        return selected_talents

    # Now add universal and rare talents into the selection pool based on checkbox values
    combined_talents = archetype_talents

    if include_universal:
        universal_talents = list(zip(universal_atfoptions['atf_name'], universal_atfoptions['atf_info'], universal_atfoptions['atf_cost']))
        combined_talents += universal_talents

    if include_rare:
        rare_talents = list(zip(rare_atfoptions['atf_name'], rare_atfoptions['atf_info'], rare_atfoptions['atf_cost']))
        combined_talents += rare_talents

    random.shuffle(combined_talents)

    # Select additional talents based on remaining points
    for name, info, cost in combined_talents:
        if remaining_points >= cost and (name, info) not in selected_talents:
            selected_talents.append((name, info))
            remaining_points -= cost

        if remaining_points == 0:
            break

    return selected_talents

# Function to generate NPC dynamically
def generate_npc(level, archetype, difficulty, is_spellcaster, include_universal, include_rare):
    # Normalize the archetype name to avoid case sensitivity or whitespace issues
    archetype = archetype.strip().lower()

    # Find the correct index for the archetype
    archetype_index = None
    for idx, name in enumerate(archestats['Archetype']):
        if name.strip().lower() == archetype:
            archetype_index = idx
            break
    
    if archetype_index is None:
        raise ValueError(f"Archetype '{archetype}' not found.")
    
    # Extract data from the updated 'archestats' dictionary for the selected archetype
    archetype_data = {key: value[archetype_index] for key, value in archestats.items()}

    # Map difficulty to appropriate keys
    perc_key = f"{difficulty}perc"
    ac_key = f"{difficulty}ac"
    dmg_key = f"{difficulty}damage"

    # Calculate HP using base HP and bonus from 'hpbonus'
    hp_column = f"Max{difficulty.capitalize()}"
    base_hp = hp[hp_column][level - 1]
    hp_bonus = archetype_data.get('hpbonus', 0) or 0  # Provide default value if hpbonus is missing or None
    total_hp = base_hp + int(hp_bonus)

    # Determine available bulk slots
    armor_bulk = archetype_data.get('armorbulk', 0) or 0  # Provide default value if armorbulk is missing or None
    bulk = archetype_data.get('bulk', 0) or 0  # Provide default value if bulk is missing or None
    available_bulk = bulk - armor_bulk


    # Define the mapping for attribute modifiers
    atbmod_mapping = {
        'atbmod1': 'highatb',
        'atbmod2': 'modatb',
        'atbmod3': 'modatb',
        'atbmod4': 'lowatb',
        'atbmod5': 'lowatb',
        'atbmod6': 'lowatb'
    }

    # Dynamic attribute assignment based on archetype
    attribute_order = ['STR', 'DEX', 'CON', 'INT', 'WIS', 'CHA']

    # Create a dictionary to hold the attribute values
    attribute_values = {}

    # Loop through each attribute (STR, DEX, etc.) and assign the correct atbmod value
    for attribute in attribute_order:
        for i in range(1, 7):  # There are 6 atbmod fields
            if archetype_data[f'atbmod{i}'] == attribute:
                mod_type = atbmod_mapping[f'atbmod{i}']
                attribute_values[attribute] = atbmods[mod_type][level - 1]
                break

    # Dynamic saving throw assignment based on archetype
    save_mapping = {
        'highsave': 'highsave',
        'modsave': 'modsave',
        'lowsave': 'lowsave'
    }

    # Create a dictionary to hold the saving throw values
    save_values = {}

    # Assign values for Fortitude, Reflex, and Will based on the archetype's save configuration
    save_values['Fort'] = savingthrows[save_mapping[archetype_data['fortsave']]][level - 1]
    save_values['Ref'] = savingthrows[save_mapping[archetype_data['refsave']]][level - 1]
    save_values['Will'] = savingthrows[save_mapping[archetype_data['willsave']]][level - 1]


    # Format NPC data
    capitalized_archetype = f"{archetype.capitalize()}"
    npc_data = (
        f"# {capitalized_archetype}\n"
        f"## **Level** {level}\n"
        f"--- \n"
        f"**Perception**: +{perception[perc_key][level - 1]} ({10 + perception[perc_key][level - 1]})\n"
        f"**AC**: {armorclass[ac_key][level - 1]}; **Fort** +{save_values['Fort']}, **Ref** +{save_values['Ref']}, **Will** +{save_values['Will']}\n"
        f"**HP:** {total_hp};\n"
        f"**Speed:** {archetype_data['speed']} ft\n"
        f"**STR** +{attribute_values['STR']}, **DEX** +{attribute_values['DEX']}, **CON** +{attribute_values['CON']}, **INT** +{attribute_values['INT']}, **WIS** +{attribute_values['WIS']}, **CHA** +{attribute_values['CHA']}\n"
        f"**Skills:** \n"
    )


    # Add skills based on skill groups dynamically using refactored keys
    skill_mapping = {
        1: 'highskill',
        2: 'modskill',
        3: 'lowskill',
        4: 'lowskill'
    }

    for i in range(1, 5):
        skill_key = f"{archetype}skill{i}"
        skill_name = skills_refactored.get(skill_key)
        if not skill_name:
            continue  # Skip if the skill is not defined

        # Get the corresponding skill value from skillmodifiers based on level
        skill_value = skillmodifiers[skill_mapping[i]][level - 1]
        npc_data += f"**{skill_name}** +{skill_value}, "

    # Add actions based on weapon groups and available bulk

    # Add talents, including optional universal and rare talents
    talents = select_talents(archetype, level, include_universal, include_rare)
    npc_data += "\n\n###### **Talents:**\n"
    if talents:
        for name, info in talents:
            npc_data += f"**{name}**: {info}\n"
    else:
        npc_data += "No talents available\n"

    # Track the number of weapons selected to determine which damage tier to use
    weapons_selected = 0

    # Initialize bulk_used before the loop
    bulk_used = 0

    # Loop through each weapon group (wep_key) defined for the archetype
    npc_data += "\n\n###### **Actions:**\n"
    for i in range(1, 5):
        wep_key = f"{archetype}_wep{i}"
        weapon_group = archweapon_groups.get(wep_key)
        if weapon_group and bulk_used < available_bulk:
            # Filter weapons by the current weapon group
            weapons_in_group = [w for w in range(len(weapons['Group'])) if weapons['Group'][w] == weapon_group]

            # Randomly shuffle the weapons in the current group
            random.shuffle(weapons_in_group)

            # Iterate over the shuffled weapons and select the first one that fits within the bulk limit
            for weapon_idx in weapons_in_group:
                weapon_bulk = weapons['Bulk'][weapon_idx]
                if bulk_used + weapon_bulk <= available_bulk:
                    weapon_data = {key: weapons[key][weapon_idx] for key in weapons.keys()}
                    
                    # Determine which damage tier to use based on the number of weapons selected
                    if weapons_selected == 0:
                        dmg_key = 'highdamage'
                    elif weapons_selected in [1, 2]:
                        dmg_key = 'moddamage'
                    else:
                        dmg_key = 'lowdamage'

                    # Generate the damage and bonus values
                    damage_string = weapondamage[dmg_key][level - 1]
                    strike_hit = extract_damage_value(damage_string)
                    bonus = int(atbmods['highatb'][level - 1]) if weapon_data['Type'] == 'Ranged' else int(atbmods['highatb'][level - 1])
                    
                    # Add the weapon to the NPC data
                    npc_data += (
                        f"**{weapon_data['Weapons']}** `[one-action]` +{strike_hit + bonus} "
                        f"[+{strike_hit + bonus - 5}/+{strike_hit + bonus - 10}] ({weapon_data['Traits']}), "
                        f"{weapon_data['Range']} {damage_string} {weapon_data['Type']}\n"
                    )
                    
                    # Increment bulk used and weapon selection count
                    bulk_used += weapon_bulk
                    weapons_selected += 1
                    break  # Stop after selecting one weapon from this group

        if bulk_used >= available_bulk:
            break  # Stop if bulk limit is reached

    # Adding spell selection if the NPC is a spellcaster
    if is_spellcaster:
        spells, used_school, secondary_school = select_spells(archetype, level)

        # Determine the appropriate DC and SAB based on difficulty
        if difficulty == 'high':
            dc = spell_stats['highdc'][level - 1]
            sab = spell_stats['highSAB'][level - 1]
        elif difficulty == 'mod':
            dc = spell_stats['moddc'][level - 1]
            sab = spell_stats['modSAB'][level - 1]
        else:  # low difficulty
            dc = spell_stats['lowdc'][level - 1]
            sab = spell_stats['lowSAB'][level - 1]

        # Determine the spell schools, display the locked-in school if 'none'
        primary_school = used_school if used_school else archestats['spell_school1'][archestats['Archetype'].index(archetype.capitalize())]
        secondary_school = secondary_school if secondary_school else archestats['spell_school2'][archestats['Archetype'].index(archetype.capitalize())]

        if primary_school == 'none':
            primary_school = "Innate"
        
        if secondary_school == 'none' or secondary_school == '0':
            school_display = f"**{primary_school} Spells**"
        else:
            school_display = f"**{primary_school} and {secondary_school} Spells**"

        npc_data += f"\n\n###### **Spells:**\n{school_display}, DC {dc}, + **{sab}**;\n"

        # Group spells by rank
        spells_by_rank = {}
        for rank, spell in spells:
            if rank not in spells_by_rank:
                spells_by_rank[rank] = []
            spells_by_rank[rank].append(spell)

        # Format the spells for output
        for rank in sorted(spells_by_rank.keys()):
            rank_spells = ', '.join([f"*{spell}*" for spell in spells_by_rank[rank]])
            npc_data += f"**R{rank}:** {rank_spells}\n"

    return npc_data


# Mapping displayed difficulty levels to internal data keys
difficulty_mapping = {
    "Low": "low",
    "Moderate": "mod",
    "High": "high"
}


#GUI Code

import sys
from PyQt5.QtWidgets import (
    QApplication, QWidget, QLabel, QVBoxLayout, 
    QHBoxLayout, QComboBox, QCheckBox, QPushButton, 
    QTextEdit, QMessageBox
)
from PyQt5.QtCore import Qt

class NPCGenerator(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Set main window properties
        self.setWindowTitle("NPC Generator")
        self.setGeometry(100, 100, 600, 700)
        self.setStyleSheet("background-color: #3B2D2D; color: #FFFFFF; font-size: 14px;")

        # Main layout
        main_layout = QVBoxLayout()

        # Stat Disposition Levels
        stat_label = QLabel("Stat Disposition Levels")
        stat_label.setStyleSheet("font-weight: bold; color: #FFFFFF; font-size: 16px; margin-bottom: 10px;")
        main_layout.addWidget(stat_label)

        # Difficulty Buttons
        self.difficulty_group = {}
        difficulty_layout = QHBoxLayout()

        self.low_button = QPushButton("Low")
        self.low_button.setStyleSheet(self.button_style(deselected=True))
        self.low_button.clicked.connect(lambda: self.toggle_buttons("Low"))
        difficulty_layout.addWidget(self.low_button)
        self.difficulty_group["Low"] = self.low_button

        self.moderate_button = QPushButton("Moderate")
        self.moderate_button.setStyleSheet(self.button_style(selected=True))
        self.moderate_button.clicked.connect(lambda: self.toggle_buttons("Moderate"))
        difficulty_layout.addWidget(self.moderate_button)
        self.difficulty_group["Moderate"] = self.moderate_button

        self.high_button = QPushButton("High")
        self.high_button.setStyleSheet(self.button_style(deselected=True))
        self.high_button.clicked.connect(lambda: self.toggle_buttons("High"))
        difficulty_layout.addWidget(self.high_button)
        self.difficulty_group["High"] = self.high_button

        difficulty_layout.setSpacing(20)
        main_layout.addLayout(difficulty_layout)

        # NPC Parameters
        param_layout = QHBoxLayout()
        param_layout.setSpacing(10)

        level_label = QLabel("Level:")
        level_label.setStyleSheet("font-weight: bold; color: #FFFFFF;")
        param_layout.addWidget(level_label)

        self.level_input = QComboBox()
        self.level_input.addItems([str(i) for i in range(1, 25)])
        self.level_input.setStyleSheet(self.combo_box_style())
        param_layout.addWidget(self.level_input)

        archetype_label = QLabel("Archetype:")
        archetype_label.setStyleSheet("font-weight: bold; color: #FFFFFF;")
        param_layout.addWidget(archetype_label)

        self.archetype_combo = QComboBox()
        self.archetype_combo.addItems(['Archer', 'Bard', 'Berserker', 'Cleric', 'Occultist', 'Paladin', 'Pugalist', 'Shaman', 'Soldier', 'Sorcerer', 'Thief', 'Wanderer', 'Wizard'])
        self.archetype_combo.setStyleSheet(self.combo_box_style())
        param_layout.addWidget(self.archetype_combo)

        main_layout.addLayout(param_layout)

        # Checkboxes
        self.spellcaster_checkbox = QCheckBox("Allow the NPC to cast Spells")
        self.spellcaster_checkbox.setStyleSheet(self.checkbox_style())
        main_layout.addWidget(self.spellcaster_checkbox)

        self.include_universal_checkbox = QCheckBox("Include Universal Talents")
        self.include_universal_checkbox.setStyleSheet(self.checkbox_style())
        main_layout.addWidget(self.include_universal_checkbox)

        self.include_rare_checkbox = QCheckBox("Include Rare Talents")
        self.include_rare_checkbox.setStyleSheet(self.checkbox_style())
        main_layout.addWidget(self.include_rare_checkbox)

        # Horizontal layout for buttons
        button_layout = QHBoxLayout()

        # Generate Button
        generate_button = QPushButton("Generate")
        generate_button.setStyleSheet(self.button_style(press_style=True))
        generate_button.clicked.connect(self.generate_npc_data)
        button_layout.addWidget(generate_button)

        # Copy to Clipboard Button
        copy_button = QPushButton("Copy to Clipboard")
        copy_button.setStyleSheet(self.button_style(press_style=True))
        copy_button.clicked.connect(self.copy_to_clipboard)
        button_layout.addWidget(copy_button)

        # Add button layout to main layout
        main_layout.addLayout(button_layout)

        # NPC Display Area
        self.npc_display = QTextEdit()
        self.npc_display.setReadOnly(True)
        self.npc_display.setStyleSheet(
            """
            background-color: #2B2B2B; 
            color: #FFFFFF; 
            border: 2px solid #5A5252; 
            border-radius: 10px; 
            padding: 10px;
            """
        )
        
        # Scrollbar Styling
        self.npc_display.verticalScrollBar().setStyleSheet(
            """
            QScrollBar:vertical {
                background: #3B2D2D;
                width: 12px;
                margin: 15px 3px 15px 3px;
                border-radius: 6px;
            }
            QScrollBar::handle:vertical {
                background: #FF4949;
                min-height: 20px;
                border-radius: 6px;
            }
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                background: none;
            }
            QScrollBar::handle:vertical:hover {
                background: #FF857B;
            }
            QScrollBar::handle:vertical:pressed {
                background: #FF4949;
            }
            """
        )
        main_layout.addWidget(self.npc_display)

        # Set the main layout and show window
        self.setLayout(main_layout)

    def button_style(self, selected=False, deselected=False, press_style=False):
        if selected:
            return """
                QPushButton {
                    background-color: #FF4949;
                    color: #FFFFFF;
                    border-radius: 15px;
                    padding: 10px 20px;
                    font-weight: bold;
                    border: 2px solid #FF857B;
                    margin: 5px;
                }
            """
        elif deselected:
            return """
                QPushButton {
                    background-color: #5A5252;
                    color: #FFFFFF;
                    border-radius: 15px;
                    padding: 10px 20px;
                    font-weight: bold;
                    border: 2px solid #5A5252;
                    margin: 5px;
                }
            """
        elif press_style:
            return """
                QPushButton {
                    background-color: #5A5252;
                    color: #FFFFFF;
                    border-radius: 15px;
                    padding: 10px 20px;
                    font-weight: bold;
                    border: 2px solid #5A5252;
                    margin: 5px;
                }
                QPushButton:pressed {
                    background-color: #FF4949;
                }
            """
        else:
            return """
                QPushButton {
                    background-color: #5A5252;
                    color: #FFFFFF;
                    border-radius: 15px;
                    padding: 10px 20px;
                    font-weight: bold;
                    border: 2px solid #5A5252;
                    margin: 5px;
                }
            """

    def toggle_buttons(self, selected):
        for key in self.difficulty_group:
            if key == selected:
                self.difficulty_group[key].setStyleSheet(self.button_style(selected=True))
            else:
                self.difficulty_group[key].setStyleSheet(self.button_style(deselected=True))

    def checkbox_style(self):
        return """
            QCheckBox {
                color: #FFFFFF;
                font-weight: bold;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border-radius: 5px;
                background-color: #5A5252;
                border: 2px solid #E6E1DC;
            }
            QCheckBox::indicator:checked {
                background-color: #FF4949;
                border-color: #FF4949;
            }
        """

    def combo_box_style(self):
        return """
            QComboBox {
                background-color: #2B2B2B;
                color: #FFFFFF;
                border-radius: 5px;
                padding: 5px;
                border: 2px solid #5A5252;
                margin: 5px;
            }
            QComboBox::drop-down {
                border: none;
            }
            QComboBox::down-arrow {
                image: url(dropdown.png); /* You can specify a custom arrow image here */
                width: 14px;
                height: 14px;
            }
            QComboBox QAbstractItemView {
                background-color: #2B2B2B;
                border-radius: 5px;
                selection-background-color: #FF4949;
                color: #FFFFFF;
            }
        """

    def generate_npc_data(self):
        level = self.level_input.currentText()
        archetype = self.archetype_combo.currentText()
        is_spellcaster = self.spellcaster_checkbox.isChecked()
        include_universal = self.include_universal_checkbox.isChecked()
        include_rare = self.include_rare_checkbox.isChecked()

        # Find the selected difficulty and map it to the correct value
        for key, button in self.difficulty_group.items():
            if button.styleSheet() == self.button_style(selected=True):
                difficulty = difficulty_mapping[key]

        # Call your existing generate_npc function
        npc_data = generate_npc(int(level), archetype, difficulty, is_spellcaster, include_universal, include_rare)

        # Display the NPC data in the text area
        self.npc_display.setPlainText(npc_data)

    def copy_to_clipboard(self):
        # Copy the NPC data to the clipboard
        clipboard = QApplication.clipboard()
        clipboard.setText(self.npc_display.toPlainText())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = NPCGenerator()
    ex.show()
    sys.exit(app.exec_())