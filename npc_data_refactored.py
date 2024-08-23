archestats = {
    'Archetype': ['Archer', 'Bard', 'Berserker', 'Cleric', 'Occultist', 'Paladin', 'Pugalist', 'Shaman', 'Soldier', 'Sorcerer', 'Thief', 'Wanderer', 'Wizard'], 
    'atbmod1': ['DEX', 'CHA', 'STR', 'WIS', 'CHA', 'STR', 'DEX', 'WIS', 'CON', 'CHA', 'DEX', 'WIS', 'INT'], 
    'atbmod2': ['WIS', 'DEX', 'CON', 'INT', 'WIS', 'CON', 'STR', 'DEX', 'STR', 'CON', 'WIS', 'DEX', 'DEX'], 
    'atbmod3': ['CON', 'INT', 'DEX', 'CON', 'CON', 'CHA', 'CON', 'INT', 'DEX', 'DEX', 'INT', 'CON', 'WIS'], 
    'atbmod4': ['STR', 'WIS', 'WIS', 'STR', 'DEX', 'DEX', 'WIS', 'CON', 'WIS', 'STR', 'CHA', 'INT', 'CON'], 
    'atbmod5': ['INT', 'CON', 'CHA', 'DEX', 'STR', 'WIS', 'INT', 'STR', 'INT', 'WIS', 'CON', 'CHA', 'CHA'], 
    'atbmod6': ['CHA', 'STR', 'INT', 'CHA', 'INT', 'INT', 'CHA', 'CHA', 'CHA', 'INT', 'STR', 'STR', 'STR'], 
    'spell_cast': ['half', 'full', 'partial', 'full', 'full', 'half', 'half', 'full', 'half', 'full', 'partial', 'partial', 'full'],
    'spell_school1':['none','Enchantment','none','Divination','Evocation','Transmutation','none','Conjuration','none','Abjuration','Illusion','Enchantment','Evocation'],
    'spell_school2':['none','Illusion','none','Abjuration','Necromancy','none','none','Evocation','none','Enchantment','none','','Enchantment'],
    'speed': [25, 25, 30, 25, 25, 20, 35, 25, 20, 25, 30, 35, 25], 
    'bulk': [4, 3, 7, 4, 3, 7, 5, 5, 5, 3, 4, 5, 3], 
    'fortsave': ['lowsave', 'lowsave', 'highsave', 'modsave', 'lowsave', 'highsave', 'modsave', 'modsave', 'highsave', 'lowsave', 'lowsave', 'modsave', 'lowsave'], 
    'refsave': ['highsave', 'modsave', 'modsave', 'lowsave', 'modsave', 'lowsave', 'modsave', 'lowsave', 'modsave', 'modsave', 'highsave', 'modsave', 'modsave'], 
    'willsave': ['modsave', 'highsave', 'lowsave', 'highsave', 'highsave', 'modsave', 'modsave', 'highsave', 'lowsave', 'highsave', 'modsave', 'highsave', 'highsave'], 
    'hpbonus': [-10, -20, 20, -15, -20, 15, 10, 0, 10, -10, -15, 0, -20], 
    'armorbulk': [2, 1, 0, 2, 0, 3, 0, 2, 2, 0, 1, 2, 0],
    }

atbmods = {
    'atblevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
    'highatb': [4, 4, 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10, 10, 10, 12], 
    'modatb': [3, 3, 3, 3, 4, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, 6, 6, 6, 7, 7, 8, 8, 9], 
    'lowatb': [1, 1, 1, 2, 2, 2, 2, 3, 3, 3, 3, 4, 4, 4, 4, 5, 5, 5, 5, 6, 6, 6, 6, 7]}

savingthrows = {
    'savelevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'highsave':[10,11,12,14,15,17,18,19,21,22,24,25,26,28,29,30,32,33,35,36,38,39,40,42],
    'modsave': [7,8,9,11,12,14,15,16,18,19,21,22,23,25,26,28,29,30,32,33,35,36,37,38],
    'lowsave': [3,4,6,7,8,11,13,14,16,17,19,20,22,23,25,26,27,28,29,30,31,32,33,34]
}

armorclass = {
    'aclevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
    'highac': [16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34, 36, 37, 39, 40, 42, 43, 45, 46, 48, 49, 51], 
    'modac': [15, 17, 18, 20, 21, 23, 24, 26, 27, 29, 30, 32, 33, 35, 36, 38, 39, 41, 42, 44, 45, 47, 48, 50], 
    'lowac': [13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34, 36, 37, 39, 40, 42, 43, 45, 46, 48]
    }

hp = {
    'hplevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
    'MaxHigh': [26, 40, 59, 78, 97, 123, 148, 173, 198, 223, 248, 273, 298, 323, 348, 373, 398, 423, 448, 473, 505, 544, 581, 633], 
    'MinHigh': [24, 36, 53, 72, 91, 115, 140, 165, 190, 215, 240, 265, 290, 315, 340, 365, 390, 415, 440, 465, 495, 532, 569, 617], 
    'MaxMod': [21, 32, 48, 63, 78, 99, 119, 139, 159, 179, 199, 219, 239, 259, 279, 299, 319, 339, 359, 379, 405, 436, 466, 508], 
    'MinMod': [19, 28, 42, 57, 72, 91, 111, 131, 151, 171, 191, 211, 231, 251, 271, 291, 311, 331, 351, 371, 395, 424, 454, 492], 
    'MaxLow': [16, 25, 37, 48, 59, 75, 90, 105, 120, 135, 150, 165, 180, 195, 210, 225, 240, 255, 270, 285, 305, 329, 351, 383], 
    'MinLow': [14, 21, 31, 42, 53, 67, 82, 97, 112, 127, 142, 157, 172, 187, 202, 217, 232, 247, 262, 277, 295, 317, 339, 367]}

perception = {
    'perclevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
    'highperc': [10, 11, 12, 14, 15, 17, 18, 19, 21, 22, 24, 25, 26, 28, 29, 30, 32, 33, 35, 36, 38, 39, 40, 42], 
    'modperc': [7, 8, 9, 11, 12, 14, 15, 16, 18, 19, 21, 22, 23, 25, 26, 28, 29, 30, 32, 33, 35, 36, 37, 38], 
    'lowperc': [4, 5, 6, 8, 9, 11, 12, 13, 15, 16, 18, 19, 20, 22, 23, 25, 26, 27, 29, 30, 32, 33, 34, 36], 
    }

# Skill Modifiers based on Level
skillmodifiers = {
    'skill_level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'highskill': [7, 8, 10, 12, 13, 15, 17, 18, 20, 22, 23, 25, 27, 28, 30, 32, 33, 35, 37, 38, 40, 42, 43, 45],
    'modskill': [6, 7, 9, 10, 12, 13, 15, 16, 18, 19, 21, 22, 24, 25, 27, 28, 30, 31, 33, 34, 36, 37, 38, 40],
    'lowskill': [3, 4, 6, 7, 8, 11, 13, 14, 16, 17, 19, 20, 22, 23, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
}

weapondamage = {
    'damagelevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24], 
    'highdamage': ['1d6+3 (6)', '1d10+4 (9)', '1d10+6 (12)', '2d8+5 (14)', '2d8+7 (16)', '2d8+9 (18)', '2d10+9 (20)', '2d10+11 (22)', '2d10+13 (24)', '2d12+13 (26)', '2d12+15 (28)', '3d10+14 (30)', '3d10+16 (32)', '3d10+18 (34)', '3d12+17 (36)', '3d12+18 (37)', '3d12+19 (38)', '3d12+20 (40)', '4d10+20 (42)', '4d10+22 (44)', '4d10+24 (46)', '4d10+26 (48)', '4d12+24 (50)', '4d12+26 (52)'], 
    'moddamage': ['1d6+2 (5)', '1d8+4 (8)', '1d8+6 (10)', '2d6+5 (12)', '2d6+6 (13)', '2d6+8 (15)', '2d8+8 (17)', '2d8+9 (18)', '2d8+11 (20)', '2d10+11 (22)', '2d10+12 (23)', '3d8+12 (25)', '3d8+14 (27)', '3d8+15 (28)', '3d10+14 (30)', '3d10+15 (31)', '3d10+16 (32)', '3d10+17 (33)', '4d8+17 (35)', '4d8+19 (37)', '4d8+20 (38)', '4d8+22 (40)', '4d10+20 (42)', '4d10+22 (44)'], 
    'lowdamage': ['1d4+2 (4)', '1d6+3 (6)', '1d6+5 (8)', '2d4+4 (9)', '2d4+6 (11)', '2d4+7 (12)', '2d6+6 (13)', '2d6+8 (15)', '2d6+9 (16)', '2d6+10 (17)', '2d8+10 (19)', '3d6+10 (20)', '3d6+11 (21)', '3d6+13 (23)', '3d6+14 (24)', '3d6+15 (25)', '3d6+16 (26)', '3d6+17 (27)', '4d6+14 (28)', '4d6+15 (29)', '4d6+17 (31)', '4d6+18 (32)', '4d6+19 (33)', '4d6+21 (35)']
    }

weapons = {
    'Weapons': ['Bastard Sword', 'Battle Axe', 'Battle lute', 'Bo Staff', 'Bola', 'Club', 'Composite Longbow', 'Composite Shortbow', 'Crossbow', 'Dagger', 'Darts', 'Falchion', 'Flail', 'Gauntlet', 'Glaive', 'Greataxe', 'Greatclub', 'Greatsword', 'Halberd', 'Hand Crossbow', 'Hatchet', 'Heavy Crossbow', 'Javelin', 'Light Hammer', 'Light mace', 'Long Hammer', 'Longbow', 'Longspear', 'Longsword', 'Mace', 'Maul', 'Morningstar', 'Scimitar', 'Scythe', 'Shield', 'Shortbow', 'Shortsword', 'Sickle', 'Sling', 'Spear', 'Spiked gauntlet', 'Staff', 'Throwing knife', 'War Pick', 'Warhammer', 'Whip'], 
    'Type': ['S', 'S', 'B', 'B', 'B', 'B', 'P', 'P', 'P', 'P', 'P', 'S', 'B', 'B', 'S', 'S', 'B', 'S', 'P', 'P', 'S', 'P', 'P', 'B', 'B', 'B', 'P', 'P', 'S', 'B', 'B', 'B', 'S', 'S', 'B', 'P', 'P', 'S', 'B', 'P', 'P', 'B', 'P', 'P', 'B', 'S'], 
    'Group': ['Sword', 'Axe', 'Club', 'Club', 'Ranged', 'Club', 'Bow', 'Bow', 'Bow', 'Knife', 'Ranged', 'Sword', 'Flail', 'Brawling', 'Polearm', 'Axe', 'Club', 'Sword', 'Polearm', 'Bow', 'Axe', 'Bow', 'Ranged', 'Hammer', 'Club', 'Hammer', 'Bow', 'Spear', 'Sword', 'Club', 'Hammer', 'Club', 'Sword', 'Polearm', 'Shield', 'Bow', 'Sword', 'Knife', 'Ranged', 'Spear', 'Brawling', 'Club', 'Knife', 'Pick', 'Hammer', 'Flail'], 
    'Traits': ['Two-hand d12', 'Sweep', 'Shove, two-hand d8', 'Parry, reach, trip', 'Nonlethal, ranged trip, thrown', 'Thrown 10 ft.', 'Deadly d10, propulsive, volley 30 ft.', 'Deadly d10, propulsive', '-', 'Agile, finesse, thrown 10 ft., versatile S', 'Agile, thrown', 'Forceful, sweep', 'Disarm, sweep, trip', 'Agile, free-hand', 'Deadly d8, forceful, reach', 'Sweep', 'Backswing, shove', 'Versatile P', 'Reach, versatile S', '-', 'Agile, sweep, thrown 10 ft.', '-', 'Thrown', 'Agile, thrown 20 ft.', 'Agile, finesse, shove', 'Brace, dwarf, reach, trip, versatile p', 'Deadly d10, volley 30 ft.', 'Reach', 'Versatile P', 'Shove', 'Shove', 'Versatile P', 'Forceful, sweep', 'Deadly d10, trip', '-', 'Deadly d10', 'Agile, finesse, versatile S', 'Agile, finesse, trip', 'Propulsive', 'Thrown 20 ft.', 'Agile, free-hand', 'Two-hand d8', 'Agile, finesse, thrown 20 ft.', 'Fatal d10', 'Shove', 'Disarm, finesse, nonlethal, reach, trip'], 
    'Range': ['-', None, None, None, '20 ft.', '10 ft.', '100 ft.', '60 ft.', '120 ft.', '10 ft.', '20 ft.', None, None, None, None, None, None, None, None, '60 ft.', '10 ft.', '120 ft.', '30 ft.', '20 ft.', '-', '-', '100 ft.', '-', '-', '-', '-', '-', '-', '-', '-', '60 ft.', '-', '-', '50 ft.', '20 ft.', '-', '-', '20 ft.', '-', '-', '-'], 
    'Bulk': [1, 1, 1, 2, 1, 1, 2, 1, 2, 1, 1, 2, 1, 1, 2, 2, 2, 2, 2, 1, 1, 2, 1, 1, 1, 2, 2, 2, 1, 1, 2, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]}

#Archtype Weapon Groups
archweapon_groups = {
    'archer_wep1': 'Bow',
    'archer_wep2': 'Knife',
    'archer_wep3': 'Axe',
    'archer_wep4': 'Ranged',
    'bard_wep1': 'Axe',
    'bard_wep2': 'Brawling',
    'bard_wep3': 'Hammer',
    'berserker_wep1': 'Axe',
    'berserker_wep2': 'Club',
    'berserker_wep3': 'Sword',
    'berserker_wep4': 'Hammer',
    'cleric_wep1': 'Hammer',
    'cleric_wep2': 'Sword',
    'cleric_wep3': 'Club',
    'occultist_wep1': 'Sword',
    'occultist_wep2': 'Axe',
    'paladin_wep1': 'Shield',
    'paladin_wep2': 'Sword',
    'paladin_wep3': 'Axe',
    'paladin_wep4': 'Hammer',    
    'pugalist_wep1': 'Brawling',
    'pugalist_wep2': 'Spear',
    'pugalist_wep3': 'Polearm',
    'pugalist_wep4': 'Sword',
    'shaman_wep1': 'Spear',
    'shaman_wep2': 'Club',
    'shaman_wep3': 'Knife',
    'soldier_wep1': 'Sword',
    'soldier_wep2': 'Hammer',
    'soldier_wep3': 'Axe',
    'soldier_wep4': 'Shield',
    'sorcerer_wep1': 'Knife',
    'sorcerer_wep1': 'Axe',
    'thief_wep1': 'Knife',
    'thief_wep2': 'Hammer',
    'thief_wep3': 'Ranged',
    'wanderer_wep1': 'Polearm',
    'wanderer_wep2': 'Ranged',
    'wanderer_wep3': 'Sword',
    'wizard_wep1': 'Knife',
    'wizard_wep2': 'Hammer',
}
# Archetype Skills

skills_refactored = {
    'archerskill1': 'Athletics',
    'archerskill2': 'Acrobatics',
    'archerskill3': 'Stealth',
    'archerskill4': 'Survial',
    'bardskill1': 'Performance',
    'bardskill2': 'Diplomacy',
    'bardskill3': 'Deception',
    'bardskill4': 'Society',
    'berserkerskill1': 'Athletics',
    'berserkerskill2': 'Intimidation',
    'berserkerskill3': 'Survival',
    'berserkerskill4': 'Acrobatics',
    'clericskill1': 'Medicine',
    'clericskill2': 'Religion',
    'clericskill3': 'Diplomacy',
    'clericskill4': 'Society',
    'occultistskill1': 'Occultism',
    'occultistskill2': 'Deception',
    'occultistskill3': 'Arcana',
    'occultistskill4': 'Diplomacy',
    'paladinskill1': 'Religion',
    'paladinskill2': 'Athletics',
    'paladinskill3': 'Intimidation',
    'paladinskill4': 'Diplomacy',    
    'pugalistskill1': 'Athletics',
    'pugalistskill2': 'Performance',
    'pugalistskill3': 'Acrobatics',
    'pugalistskill4': 'Medicine',
    'shamanskill1': 'Nature',
    'shamanskill2': 'Survival',
    'shamanskill3': 'Medicine',
    'shamanskill4': 'Religion',
    'soldierskill1': 'Athletics',
    'soldierskill2': 'Intimidation',
    'soldierskill3': 'Survival',
    'soldierskill4': 'Medicine',
    'sorcererskill1': 'Arcana',
    'sorcererskill1': 'Deception',
    'sorcererskill1': 'Diplomacy',
    'sorcererskill1': 'Intimidation',
    'thiefskill1': 'Stealth',
    'thiefskill2': 'Thievery',
    'thiefskill3': 'Acrobatics',
    'thiefskill4': 'Deception',
    'wandererskill1': 'Survival',
    'wandererskill2': 'Nature',
    'wandererskill3': 'Acrobatics',
    'wandererskill4': 'Occultism',
    'wizardskill1': 'Arcana',
    'wizardskill2': 'Crafting',
    'wizardskill3': 'Occultism',
    'wizardskill4': 'Soceity',
}


#Spell Data

archetype_casting = {
'casting_school': ['Abjuration','Conjuration','Divination','Enchantment','Evocation','Illusion','Necromancy','Transmutation'],
}

spell_stats = {
    'spelllevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'highdc': [20,22,23,25,26,27,29,30,32,33,34,36,37,39,40,41,43,44,46,47,48,50,51,52],
    'moddc': [17,18,20,21,22,24,25,26,28,29,30,32,33,34,36,37,38,40,41,42,44,45,46,48],
    'lowdc': [14,15,17,18,19,21,22,23,25,26,27,29,30,31,33,34,35,37,38,39,41,42,43,45],
    'highSAB':[12,14,15,17,18,19,21,22,24,25,26,28,29,31,32,33,35,36,38,39,40,42,43,44],
    'modSAB':[9,10,12,13,14,16,17,18,20,21,22,24,25,26,28,29,30,32,33,34,36,37,38,40],
    'lowSAB':[6,7,9,10,11,13,14,15,17,18,19,21,22,23,25,26,27,29,30,31,33,34,35,37],
}

fullcaster_spellslots = {
    'casterlevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'rank0_total': [5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5,5],
    'rank1_total': [2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    'rank2_total': [0,0,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    'rank3_total': [0,0,0,0,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    'rank4_total': [0,0,0,0,0,0,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],    
    'rank5_total': [0,0,0,0,0,0,0,0,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3], 
    'rank6_total': [0,0,0,0,0,0,0,0,0,0,2,3,3,3,3,3,3,3,3,3,3,3,3,3],
    'rank7_total': [0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,3,3,3,3,3,3,3,3,3],
    'rank8_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,3,3,3,3,3,3,3],
    'rank9_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2,3,3,3,3,3,3,3],
    'rank10_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2],

}

halfcaster_spellslots = {
    'casterlevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'rank0_total': [1,1,1,1,2,2,2,2,3,3,3,3,4,4,4,4,5,5,5,5,5,5,5,5],
    'rank1_total': [1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    'rank2_total': [0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3],
    'rank3_total': [0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3,3,3],
    'rank4_total': [0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3,3,3,3],    
    'rank5_total': [0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3,3,3], 
    'rank6_total': [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2,3,3,3,3],
    'rank7_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,3],
    'rank8_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2,2,2],
    'rank9_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,2,2],
    'rank10_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
}

partialcaster_spellslots = {
    'casterlevel': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'rank0_total': [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    'rank1_total': [1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3,3,3,3,3,3,3],
    'rank2_total': [0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,3],
    'rank3_total': [0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3,3,3],
    'rank4_total': [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3,3,3],    
    'rank5_total': [0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2,2,2,3,3], 
    'rank6_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,2,2,2,2],
    'rank7_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2,2,2],
    'rank8_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,2],
    'rank9_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1],
    'rank10_total': [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1],

}

spell_list = {
# Cantrips
    'rank_0': [
        'Caustic Blast',
        'Daze',
        'Detect Magic',
        'Divine Lance',
        'Electric Arc',
        'Figment',
        'Forbidding Ward',
        'Frostbite',
        'Gouging Claw',
        'Guidance',
        'Ignition',
        'Know the Way',
        'Light',
        'Message',
        'Prestidigitation',
        'Read Aura',
        'Shield',
        'Sigil',
        'Stabilize',
        'Summon Instrument',
        'Tangle Vine',
        'Telekinetic Hand',
        'Telekinetic Projectile',
        'Vitality Lash',
        'Void Warp',
        'Ventriloquism'
    ],

    'rank_0_school': [
        'Evocation',  # Caustic Blast
        'Enchantment',  # Daze
        'Divination',  # Detect Magic
        'Evocation',  # Divine Lance
        'Evocation',  # Electric Arc
        'Illusion',  # Figment
        'Abjuration',  # Forbidding Ward
        'Evocation',  # Frostbite
        'Transmutation',  # Gouging Claw
        'Divination',  # Guidance
        'Evocation',  # Ignition
        'Divination',  # Know the Way
        'Evocation',  # Light
        'Divination',  # Message
        'Transmutation',  # Prestidigitation
        'Divination',  # Read Aura
        'Abjuration',  # Shield
        'Illusion',  # Sigil
        'Necromancy',  # Stabilize
        'Conjuration',  # Summon Instrument
        'Transmutation',  # Tangle Vine
        'Transmutation',  # Telekinetic Hand
        'Evocation',  # Telekinetic Projectile
        'Necromancy',  # Vitality Lash
        'Transmutation',  # Void Warp
        'Illusion'  # Ventriloquism
    ],
# Rank 1

    'rank_1': [
        'Air Bubble',
        'Alarm',
        'Animate Rope',
        'Ant Haul',
        'Bane',
        'Bless',
        'Breathe Fire',
        'Charm',
        'Chilling Spray',
        'Cleanse Cuisine',
        'Command',
        'Create Water',
        'Disguise Magic',
        'Dizzying Colors',
        'Déjà Vu',
        'Enfeeble',
        'Fear',
        'Fleet Step',
        'Force Barrage',
        'Gentle Landing',
        'Goblin Pox',
        'Grease',
        'Grim Tendrils',
        'Gust of Wind',
        'Harm',
        'Heal',
        'Hydraulic Push',
        'Ill Omen',
        'Illusory Disguise',
        'Illusory Object',
        'Imprint Message',
        'Infuse Vitality',
        'Invisible Item',
        'Item Facade',
        'Jump',
        'Lock',
        'Magic Stone',
        'Mending',
        'Mindlink',
        'Mystic Armor',
        'Noxious Vapors',
        'Object Reading',
        'Pest Form',
        'Pet Cache',
        'Phantasmal Minion',
        'Phantom Pain',
        'Protection',
        'Pummeling Rubble',
        'Runic Body',
        'Runic Weapon',
        'Sanctuary',
        'Sleep',
        'Soothe',
        'Spider Sting',
        'Spirit Link',
        'Summon Animal',
        'Summon Construct',
        'Summon Fey',
        'Summon Plant or Fungus',
        'Summon Undead',
        'Sure Strike',
        'Tailwind',
        'Thoughtful Gift',
        'Thunderstrike',
        'Vanishing Tracks',
        'Ventriloquism'
    ],

    'rank_1_school': [
        'Transmutation',  # Air Bubble
        'Abjuration',  # Alarm
        'Transmutation',  # Animate Rope
        'Transmutation',  # Ant Haul
        'Enchantment',  # Bane
        'Enchantment',  # Bless
        'Evocation',  # Breathe Fire
        'Enchantment',  # Charm
        'Evocation',  # Chilling Spray
        'Abjuration',  # Cleanse Cuisine
        'Enchantment',  # Command
        'Conjuration',  # Create Water
        'Illusion',  # Disguise Magic
        'Illusion',  # Dizzying Colors
        'Divination',  # Déjà Vu
        'Necromancy',  # Enfeeble
        'Enchantment',  # Fear
        'Transmutation',  # Fleet Step
    ],
# Rank 2  
 
    'rank_2': [
        'Acid Grip',
        'Animal Form',
        'Animal Messenger',
        'Animated Assault',
        'Augury',
        'Blazing Bolt',
        'Blistering Invective',
        'Blood Vendetta',
        'Blur',
        'Calm',
        'Charitable Urge',
        'Cleanse Affliction',
        'Clear Mind',
        'Create Food',
        'Darkness',
        'Darkvision',
        'Deafness',
        'Dismantle',
        'Dispel Magic',
        'Embed Message',
        'Enlarge',
        'Entangling Flora',
        'Environmental Endurance',
        'Everlight',
        'False Vitality',
        'Final Sacrifice',
        'Floating Flame',
        'Fungal Infestation',
        'Gecko Grip',
        'Ghostly Carrier',
        'Heat Metal',
        'Humanoid Form',
        'Illusory Creature',
        'Invisibility',
        'Knock',
        'Laughing Fit',
        'Marvelous Mount',
        'Mist',
        'Noise Blast',
        'Oaken Resilience',
        'One with Plants',
        'Paranoia',
        'Peaceful Rest',
        'Phantasmal Treasure',
        'Quench',
        'Reaper\'s Lantern',
        'Resist Energy',
        'Revealing Light',
        'See the Unseen',
        'Shape Wood',
        'Share Life',
        'Shatter',
        'Shrink',
        'Silence',
        'Sound Body',
        'Speak with Animals',
        'Spirit Sense',
        'Spiritual Armament',
        'Status',
        'Stupefy',
        'Sudden Blight',
        'Summon Elemental',
        'Sure Footing',
        'Telekinetic Maneuver',
        'Translate',
        'Vomit Swarm',
        'Water Breathing',
        'Water Walk'
    ],

    'rank_2_school': [
        'Evocation',  # Acid Grip
        'Transmutation',  # Animal Form
        'Conjuration',  # Animal Messenger
        'Evocation',  # Animated Assault
        'Divination',  # Augury
        'Evocation',  # Blazing Bolt
        'Enchantment',  # Blistering Invective
        'Necromancy',  # Blood Vendetta
        'Illusion',  # Blur
        'Enchantment',  # Calm
        'Enchantment',  # Charitable Urge
        'Abjuration',  # Cleanse Affliction
        'Divination',  # Clear Mind
        'Conjuration',  # Create Food
        'Evocation',  # Darkness
        'Transmutation',  # Darkvision
        'Necromancy',  # Deafness
        'Transmutation',  # Dismantle
        'Abjuration',  # Dispel Magic
        'Divination',  # Embed Message
        'Transmutation',  # Enlarge
        'Conjuration',  # Entangling Flora
        'Abjuration',  # Environmental Endurance
        'Evocation',  # Everlight
        'Necromancy',  # False Vitality
        'Evocation',  # Final Sacrifice
        'Evocation',  # Floating Flame
        'Necromancy',  # Fungal Infestation
        'Transmutation',  # Gecko Grip
        'Conjuration',  # Ghostly Carrier
        'Transmutation',  # Heat Metal
        'Transmutation',  # Humanoid Form
        'Illusion',  # Illusory Creature
        'Illusion',  # Invisibility
        'Transmutation',  # Knock
        'Enchantment',  # Laughing Fit
        'Conjuration',  # Marvelous Mount
        'Conjuration',  # Mist
        'Evocation',  # Noise Blast
        'Transmutation',  # Oaken Resilience
        'Transmutation',  # One with Plants
        'Enchantment',  # Paranoia
        'Necromancy',  # Peaceful Rest
        'Illusion',  # Phantasmal Treasure
        'Abjuration',  # Quench
        'Necromancy',  # Reaper's Lantern
        'Abjuration',  # Resist Energy
        'Evocation',  # Revealing Light
        'Divination',  # See the Unseen
        'Transmutation',  # Shape Wood
        'Necromancy',  # Share Life
        'Evocation',  # Shatter
        'Transmutation',  # Shrink
        'Illusion',  # Silence
        'Transmutation',  # Sound Body
        'Divination',  # Speak with Animals
        'Divination',  # Spirit Sense
        'Transmutation',  # Spiritual Armament
        'Divination',  # Status
        'Necromancy',  # Stupefy
        'Necromancy',  # Sudden Blight
        'Conjuration',  # Summon Elemental
        'Transmutation',  # Sure Footing
        'Transmutation',  # Telekinetic Maneuver
        'Divination',  # Translate
        'Necromancy',  # Vomit Swarm
        'Transmutation',  # Water Breathing
        'Transmutation'  # Water Walk
    ],
# Rank 3

    'rank_3': [
        'Agonizing Despair',
        'Aqueous Orb',
        'Bind Undead',
        'Blindness',
        'Chilling Darkness',
        'Clairaudience',
        'Cozy Cabin',
        'Crashing Wave',
        'Crisis of Faith',
        'Curse of Lost Time',
        'Dream Message',
        'Earthbind',
        'Enthrall',
        'Familiar\'s Face',
        'Feet to Fins',
        'Fireball',
        'Ghostly Weapon',
        'Haste',
        'Heroism',
        'Holy Light',
        'Hypercognition',
        'Hypnotize',
        'Insect Form',
        'Levitate',
        'Lightning Bolt',
        'Mad Monkeys',
        'One with Stone',
        'Paralyze',
        'Safe Passage',
        'Sculpt Sound',
        'Slow',
        'Speak with Plants',
        'Threefold Aspect',
        'Vampiric Feast',
        'Wall of Thorns',
        'Wall of Wind'
    ],

    'rank_3_school': [
        'Enchantment',  # Agonizing Despair
        'Conjuration',  # Aqueous Orb
        'Necromancy',  # Bind Undead
        'Necromancy',  # Blindness
        'Necromancy',  # Chilling Darkness
        'Divination',  # Clairaudience
        'Conjuration',  # Cozy Cabin
        'Evocation',  # Crashing Wave
        'Enchantment',  # Crisis of Faith
        'Necromancy',  # Curse of Lost Time
        'Divination',  # Dream Message
        'Transmutation',  # Earthbind
        'Enchantment',  # Enthrall
        'Divination',  # Familiar's Face
        'Transmutation',  # Feet to Fins
        'Evocation',  # Fireball
        'Necromancy',  # Ghostly Weapon
        'Transmutation',  # Haste
        'Enchantment',  # Heroism
        'Evocation',  # Holy Light
        'Divination',  # Hypercognition
        'Enchantment',  # Hypnotize
        'Transmutation',  # Insect Form
        'Transmutation',  # Levitate
        'Evocation',  # Lightning Bolt
        'Conjuration',  # Mad Monkeys
        'Transmutation',  # One with Stone
        'Enchantment',  # Paralyze
        'Abjuration',  # Safe Passage
        'Illusion',  # Sculpt Sound
        'Transmutation',  # Slow
        'Divination',  # Speak with Plants
        'Transmutation',  # Threefold Aspect
        'Necromancy',  # Vampiric Feast
        'Conjuration',  # Wall of Thorns
        'Evocation'  # Wall of Wind
    ],
# Rank 4

    'rank_4': [
        'Aerial Form',
        'Bestial Curse',
        'Chroma Leech',
        'Clairvoyance',
        'Confusion',
        'Countless Eyes',
        'Creation',
        'Dinosaur Form',
        'Divine Wrath',
        'Dull Ambition',
        'Enervation',
        'Fire Shield',
        'Flicker',
        'Fly',
        'Honeyed Words',
        'Hydraulic Torrent',
        'Ice Storm',
        'Mountain Resilience',
        'Nightmare',
        'Outcast\'s Curse',
        'Planar Tether',
        'Rusting Grasp',
        'Seal Fate',
        'Shape Stone',
        'Spike Stones',
        'Suggestion',
        'Telepathy',
        'Translocate',
        'Unfettered Movement',
        'Vampiric Maiden',
        'Vapor Form',
        'Vision of Death',
        'Vital Beacon',
        'Wall of Fire',
        'Weapon Storm'
    ],

    'rank_4_school': [
            'Transmutation',  # Aerial Form
            'Necromancy',  # Bestial Curse
            'Necromancy',  # Chroma Leech
            'Divination',  # Clairvoyance
            'Enchantment',  # Confusion
            'Transmutation',  # Countless Eyes
            'Conjuration',  # Creation
            'Transmutation',  # Dinosaur Form
            'Evocation',  # Divine Wrath
            'Enchantment',  # Dull Ambition
            'Necromancy',  # Enervation
            'Evocation',  # Fire Shield
            'Illusion',  # Flicker
            'Transmutation',  # Fly
            'Enchantment',  # Honeyed Words
            'Evocation',  # Hydraulic Torrent
            'Evocation',  # Ice Storm
            'Transmutation',  # Mountain Resilience
            'Illusion',  # Nightmare
            'Necromancy',  # Outcast's Curse
            'Conjuration',  # Planar Tether
            'Transmutation',  # Rusting Grasp
            'Necromancy',  # Seal Fate
            'Transmutation',  # Shape Stone
            'Transmutation',  # Spike Stones
            'Enchantment',  # Suggestion
            'Divination',  # Telepathy
            'Conjuration',  # Translocate
            'Transmutation',  # Unfettered Movement
            'Necromancy',  # Vampiric Maiden
            'Transmutation',  # Vapor Form
            'Necromancy',  # Vision of Death
            'Necromancy',  # Vital Beacon
            'Evocation',  # Wall of Fire
            'Evocation'  # Weapon Storm
        ],
# Rank 5

    'rank_5': [
        'Banishment',
        'Blister',
        'Breath of Life',
        'Chameleon Coat',
        'Control Water',
        'Divine Immolation',
        'Dreaming Potential',
        'Elemental Form',
        'Grisly Growths',
        'Hallucination',
        'Howling Blizzard',
        'Illusory Scene',
        'Impaling Spike',
        'Invoke Spirits',
        'Lightning Storm',
        'Mariner\'s Curse',
        'Moon Frenzy',
        'Plant Form',
        'Scouting Eye',
        'Secret Chest',
        'Sending',
        'Shadow Blast',
        'Slither',
        'Speak with Stones',
        'Spiritual Guardian',
        'Strange Geometry',
        'Subconscious Suggestion',
        'Summon Celestial',
        'Summon Dragon',
        'Summon Entity',
        'Summon Fiend',
        'Summon Giant',
        'Summon Monitor',
        'Synaptic Pulse',
        'Telekinetic Haul',
        'Toxic Cloud',
        'Transmute Rock and Mud',
        'Wall of Flesh',
        'Wall of Ice',
        'Wall of Stone',
        'Wave of Despair'
    ],

    'rank_5_school': [
        'Abjuration',  # Banishment
        'Necromancy',  # Blister
        'Necromancy',  # Breath of Life
        'Transmutation',  # Chameleon Coat
        'Transmutation',  # Control Water
        'Evocation',  # Divine Immolation
        'Divination',  # Dreaming Potential
        'Transmutation',  # Elemental Form
        'Necromancy',  # Grisly Growths
        'Illusion',  # Hallucination
        'Evocation',  # Howling Blizzard
        'Illusion',  # Illusory Scene
        'Transmutation',  # Impaling Spike
        'Necromancy',  # Invoke Spirits
        'Evocation',  # Lightning Storm
        'Necromancy',  # Mariner's Curse
        'Transmutation',  # Moon Frenzy
        'Transmutation',  # Plant Form
        'Divination',  # Scouting Eye
        'Conjuration',  # Secret Chest
        'Divination',  # Sending
        'Evocation',  # Shadow Blast
        'Transmutation',  # Slither
        'Divination',  # Speak with Stones
        'Conjuration',  # Spiritual Guardian
        'Illusion',  # Strange Geometry
        'Enchantment',  # Subconscious Suggestion
        'Conjuration',  # Summon Celestial
        'Conjuration',  # Summon Dragon
        'Conjuration',  # Summon Entity
        'Conjuration',  # Summon Fiend
        'Conjuration',  # Summon Giant
        'Conjuration',  # Summon Monitor
        'Evocation',  # Synaptic Pulse
        'Transmutation',  # Telekinetic Haul
        'Evocation',  # Toxic Cloud
        'Transmutation',  # Transmute Rock and Mud
        'Necromancy',  # Wall of Flesh
        'Evocation',  # Wall of Ice
        'Transmutation',  # Wall of Stone
        'Enchantment'  # Wave of Despair
    ],
# Rank 6

    'rank_6': [
        'Blanket of Stars',
        'Blessed Boundary',
        'Blinding Fury',
        'Chain Lightning',
        'Cursed Metamorphosis',
        'Disintegrate',
        'Dragon Form',
        'Field of Life',
        'Mislead',
        'Never Mind',
        'Petrify',
        'Phantasmal Calamity',
        'Repulsion',
        'Scintillating Safeguard',
        'Spellwrack',
        'Spirit Blast',
        'Tangling Creepers',
        'Tree of Seasons',
        'Truesight',
        'Vampiric Exsanguination',
        'Vibrant Pattern',
        'Wall of Force',
        'Zealous Conviction'
    ],

    'rank_6_school': [
        'Illusion',  # Blanket of Stars
        'Abjuration',  # Blessed Boundary
        'Enchantment',  # Blinding Fury
        'Evocation',  # Chain Lightning
        'Transmutation',  # Cursed Metamorphosis
        'Transmutation',  # Disintegrate
        'Transmutation',  # Dragon Form
        'Necromancy',  # Field of Life
        'Illusion',  # Mislead
        'Enchantment',  # Never Mind
        'Transmutation',  # Petrify
        'Illusion',  # Phantasmal Calamity
        'Abjuration',  # Repulsion
        'Abjuration',  # Scintillating Safeguard
        'Abjuration',  # Spellwrack
        'Necromancy',  # Spirit Blast
        'Conjuration',  # Tangling Creepers
        'Transmutation',  # Tree of Seasons
        'Divination',  # Truesight
        'Necromancy',  # Vampiric Exsanguination
        'Illusion',  # Vibrant Pattern
        'Evocation',  # Wall of Force
        'Enchantment'  # Zealous Conviction
    ],
# Rank 7

    'rank_7': [
        'Contingency',
        'Divine Decree',
        'Duplicate Foe',
        'Eclipse Burst',
        'Energy Aegis',
        'Execute',
        'Fiery Body',
        'Force Cage',
        'Mask of Terror',
        'Project Image',
        'Regenerate',
        'Retrocognition',
        'Sunburst',
        'True Target',
        'Unfettered Pack',
        'Volcanic Eruption',
        'Warp Mind'
    ],

    'rank_7_school': [
        'Abjuration',  # Contingency
        'Evocation',  # Divine Decree
        'Illusion',  # Duplicate Foe
        'Evocation',  # Eclipse Burst
        'Abjuration',  # Energy Aegis
        'Necromancy',  # Execute
        'Transmutation',  # Fiery Body
        'Evocation',  # Force Cage
        'Illusion',  # Mask of Terror
        'Illusion',  # Project Image
        'Necromancy',  # Regenerate
        'Divination',  # Retrocognition
        'Evocation',  # Sunburst
        'Divination',  # True Target
        'Transmutation',  # Unfettered Pack
        'Evocation',  # Volcanic Eruption
        'Enchantment'  # Warp Mind
    ],
# Rank 8

    'rank_8': [
        'Arctic Rift',
        'Canticle of Everlasting Grief',
        'Desiccate',
        'Disappearance',
        'Divine Inspiration',
        'Earthquake',
        'Migration',
        'Moment of Renewal',
        'Monstrosity Form',
        'Punishing Winds',
        'Quandary',
        'Uncontrollable Dance',
        'Unrelenting Observation'
    ],

    'rank_8_school': [
        'Evocation',  # Arctic Rift
        'Enchantment',  # Canticle of Everlasting Grief
        'Necromancy',  # Desiccate
        'Illusion',  # Disappearance
        'Divination',  # Divine Inspiration
        'Evocation',  # Earthquake
        'Conjuration',  # Migration
        'Necromancy',  # Moment of Renewal
        'Transmutation',  # Monstrosity Form
        'Evocation',  # Punishing Winds
        'Enchantment',  # Quandary
        'Enchantment',  # Uncontrollable Dance
        'Divination'  # Unrelenting Observation
    ],
# Rank 9

    'rank_9': [
        'Falling Stars',
        'Foresight',
        'Implosion',
        'Massacre',
        'Metamorphosis',
        'Overwhelming Presence',
        'Phantasmagoria',
        'Unfathomable Song',
        'Wails of the Damned',
        'Wrathful Storm'
    ],

    'rank_9_school': [
        'Evocation',  # Falling Stars
        'Divination',  # Foresight
        'Evocation',  # Implosion
        'Necromancy',  # Massacre
        'Transmutation',  # Metamorphosis
        'Enchantment',  # Overwhelming Presence
        'Illusion',  # Phantasmagoria
        'Enchantment',  # Unfathomable Song
        'Necromancy',  # Wails of the Damned
        'Evocation'  # Wrathful Storm
    ],
# Rank 10

    'rank_10': [
        'Avatar',
        'Cataclysm',
        'Fabricated Truth',
        'Freeze Time',
        'Indestructibility',
        'Manifestation',
        'Nature Incarnate',
        'Revival'
    ],

    'rank_10_school': [
        'Transmutation',  # Avatar
        'Evocation',  # Cataclysm
        'Illusion',  # Fabricated Truth
        'Transmutation',  # Freeze Time
        'Transmutation',  # Indestructibility
        'Conjuration',  # Manifestation
        'Transmutation',  # Nature Incarnate
        'Necromancy'  # Revival
    ],  
}


# Abilities, Talents and Feats by Archetype

atfpointbuy = {
    'archetype_level': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24],
    'atf_points': [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12],
}

archer_atfoptions = {
   'atf_name' : [
      "Point-Blank Shot",
      "Deadly Aim",
      "Double Shot",
      "Precision Strike",
      "Hunter's Aim",
      "Quick Draw",
      "Parting Shot",
      "Pinning Shot",
      "Sniper's Aim",
      "Ricochet Shot",
      "Arrow Rain",
      "Disrupting Shot",
      "Arrow Snatch",
      "Wind Runner",
      "Focused Fire"
   ],
   'atf_info' : [
      "+1 bonus to attack rolls with a ranged weapon within 30 feet.", # Point-Blank Shot
      "Take a -2 penalty to attack roll to deal an additional 1d6 damage.", # Deadly Aim
      "Fire two arrows at once; both attacks suffer a -2 penalty.", # Double Shot
      "+2 circumstance bonus to damage against a targeted creature.", # Precision Strike
      "Reduce the target's cover bonuses by 2 for your next attack.", # Hunter's Aim
      "Draw and fire a bow as part of the same action.", # Quick Draw
      "Make a ranged Strike as a free action when you take the Step action.", # Parting Shot
      "Hit a creature to reduce their speed by 10 feet for 1 round.", # Pinning Shot
      "+1 circumstance bonus to attack rolls when you have 1 minute to set up and are not observed.", # Sniper's Aim
      "Redirect a missed attack to another creature within 10 feet; make a new attack roll.", # Ricochet Shot
      "Strike against every enemy within a 15-foot cone; attacks suffer a -2 penalty.", # Arrow Rain
      "On a hit, target must succeed on a concentration check or lose the spell.", # Disrupting Shot
      "Make a Reflex save (DC equals the attack roll) to catch an arrow or bolt.", # Arrow Snatch
      "+10-foot bonus to movement speed when moving in a straight line.", # Wind Runner
      "Deal an extra 1d6 damage after focusing on a target for 1 round." # Focused Fire
   ],
   'atf_cost' : [
      2, 3, 3, 2, 2, 2, 2, 2, 2, 3, 3, 3, 2, 2, 3
   ]
}

bard_atfoptions = {
   'atf_name' : [
      "Inspire Courage",
      "Dirge of Doom",
      "Fascinate",
      "Lingering Composition",
      "Inspire Competence",
      "Soothing Ballad",
      "Counter Performance",
      "Inspire Heroics",
      "Song of Strength",
      "Hymn of Healing",
      "Encore Performance",
      "Masterful Melody",
      "Quickened Casting",
      "Triple Time",
      "Harmonize"
   ],
   'atf_info' : [
      "Allies gain a +1 status bonus to attack rolls, damage rolls, and saves against fear for 1 round.", # Inspire Courage
      "Enemies within 30 feet are frightened 1.", # Dirge of Doom
      "Target must succeed at a Will save or become fascinated.", # Fascinate
      "Make a Performance check (DC 20) to extend the duration of a composition cantrip by 3 rounds.", # Lingering Composition
      "Ally gains a +1 status bonus to skill checks for 1 round.", # Inspire Competence
      "Allies regain d6 equal to half level (min 1d6) Hit Points at the start of each of your turns for 3 rounds.", # Soothing Ballad
      "Allies can use your Performance check result in place of their saving throw against auditory or visual effects.", # Counter Performance
      "Allies gain a +2 status bonus to attack rolls, damage rolls, and saves against fear for 1 round.", # Inspire Heroics
      "Grant an ally a +2 circumstance bonus to Athletics checks for 1 round.", # Song of Strength
      "Heal an ally for 1d8 Hit Points per action spent (up to 3 actions).", # Hymn of Healing
      "Gain an extra use of a composition cantrip that you've already used this turn.", # Encore Performance
      "Increase the area of your composition cantrips by 10 feet.", # Masterful Melody
      "Cast a composition cantrip as a free action once per day.", # Quickened Casting
      "Allies gain a +10-foot status bonus to their Speed for 1 round.", # Triple Time
      "Maintain two composition simultaneously." # Harmonize
   ],
   'atf_cost' : [
      2, 3, 2, 3, 2, 3, 3, 3, 2, 3, 3, 2, 3, 2, 3
   ]
}

berserker_atfoptions = {
   'atf_name' : [
      "Rage",
      "Power Attack",
      "Furious Charge",
      "Raging Resistance",
      "Furious Focus",
      "Savage Critical",
      "Raging Brutality",
      "Battle Cry",
      "Intimidating Glare",
      "Destructive Impulse",
      "Bloody Rampage",
      "Unstoppable",
      "Raging Throw",
      "Brutal Bulwark",
      "Mighty Rage"
   ],
   'atf_info' : [
      "Gain +2 status bonus to damage rolls, -1 penalty to AC, lasts 1 minute.", # Rage
      "Make a single melee Strike with a +2 bonus to damage; counts as two attacks for your multiple attack penalty.", # Power Attack
      "Stride and then make a melee Strike; gain a +1 circumstance bonus to attack roll.", # Furious Charge
      "Gain resistance to physical damage equal to 3 + your Constitution modifier while raging.", # Raging Resistance
      "Ignore the multiple attack penalty on your second attack after making a Power Attack.", # Furious Focus
      "When you critically hit while raging, add an additional weapon damage die.", # Savage Critical
      "Add your Strength modifier twice to the damage of your first melee attack each round while raging.", # Raging Brutality
      "When you roll initiative, Demoralize a foe within 30 feet as a free action.", # Battle Cry
      "Demoralize a foe with a visual glare instead of verbal threats; no language requirement.", # Intimidating Glare
      "Gain a +2 circumstance bonus to Strength checks to break objects while raging.", # Destructive Impulse
      "When you reduce a creature to 0 Hit Points, make a melee Strike as a free action.", # Bloody Rampage
      "Gain temporary Hit Points equal to 10 + your level when you begin raging.", # Unstoppable
      "Throw an adjacent enemy, dealing bludgeoning damage equal to 1d6 + your Strength modifier.", # Raging Throw
      "Gain a +2 circumstance bonus to Fortitude saves against effects that would push, trip, or grapple you while raging.", # Brutal Bulwark
      "Increase the bonus from Rage to +3 status bonus to damage rolls." # Mighty Rage
   ],
   'atf_cost' : [
      3, 3, 2, 3, 2, 3, 3, 2, 2, 2, 3, 3, 2, 2, 3
   ]
}

cleric_atfoptions = {
   'atf_name' : [
      "Channel Energy",
      "Domain Initiate",
      "Turn Undead",
      "Harm Undead",
      "Divine Font",
      "Holy Castigation",
      "Selective Energy",
      "Divine Weapon",
      "Rebuke Death",
      "Ward Against Death",
      "Command Undead",
      "Divine Shield",
      "Holy Nimbus",
      "Sacred Defense",
      "Healing Hands"
   ],
   'atf_info' : [
      "Heal living or harm undead within 30 feet for 1d8 Hit Points per level of the spell slot expended.", # Channel Energy
      "Gain the initial domain power associated with your deity's domain.", # Domain Initiate
      "Undead creatures within 30 feet must succeed at a Will save or flee for 1d4 rounds.", # Turn Undead
      "Undead creatures within 30 feet take 1d6 damage per level of the spell slot expended.", # Harm Undead
      "Gain an additional spell slot for heal or harm, depending on your deity's alignment.", # Divine Font
      "Gain a +1 status bonus to attack rolls and damage rolls against evil creatures.", # Holy Castigation
      "Exclude a number of targets equal to your Charisma modifier from your Channel Energy effect.", # Selective Energy
      "Grant a weapon within 30 feet a +1 striking rune for 1 minute.", # Divine Weapon
      "Stabilize a dying creature within 30 feet as a free action.", # Rebuke Death
      "Gain a +2 status bonus to saving throws against death effects and negative energy.", # Ward Against Death
      "Take control of an undead creature within 30 feet; it must succeed at a Will save or fall under your command.", # Command Undead
      "Gain a +2 status bonus to AC for 1 round.", # Divine Shield
      "Emit bright light in a 20-foot radius; creatures within the light gain a +1 status bonus to saving throws against fear and death effects.", # Holy Nimbus
      "Allies within 30 feet gain a +1 status bonus to AC for 1 round.", # Sacred Defense
      "When you cast heal, increase the amount of healing by 2d8." # Healing Hands
   ],
   'atf_cost' : [
      1, 2, 3, 3, 3, 2, 2, 3, 2, 2, 3, 2, 3, 2, 3
   ]
}

occultist_atfoptions = {
   'atf_name' : [
      "Occult Implements",
      "Resonant Power",
      "Mental Shield",
      "Object Reading",
      "Focus Catharsis",
      "Psychic Resonance",
      "Esoteric Lore",
      "Mind's Eye",
      "Arcane Sight",
      "Symbolic Link",
      "Eldritch Understanding",
      "Mental Fortress",
      "Astral Projection",
      "Occult Defense",
      "Sigil Mastery"
   ],
   'atf_info' : [
      "Gain access to one occult implement, granting you an additional ability based on the implement chosen.", # Occult Implements
      "Gain a +1 status bonus to attacks or spell DCs when wielding your chosen occult implement.", # Resonant Power
      "Gain a +2 circumstance bonus to saving throws against mental effects while concentrating.", # Mental Shield
      "Spend 1 minute concentrating on an object to gain insight into its history and previous owners (Recall Knowledge).", # Object Reading
      "Regain 1 Focus Point when you critically succeed at a save against a mental effect.", # Focus Catharsis
      "Gain a +1 circumstance bonus to damage with occult spells when you are affected by a mental effect.", # Psychic Resonance
      "Gain a +1 circumstance bonus to Occultism checks and to checks to identify occult creatures or phenomena.", # Esoteric Lore
      "Detect invisible creatures within 30 feet as if you had imprecise senses.", # Mind's Eye
      "Once per day, you can cast detect magic as a free action.", # Arcane Sight
      "When you possess a significant item from a creature, gain a +2 circumstance bonus to checks to locate or affect that creature with spells.", # Symbolic Link
      "Gain a +1 status bonus to DCs of occult rituals you perform.", # Eldritch Understanding
      "Gain resistance to mental damage equal to half your level.", # Mental Fortress
      "Once per day, project your mind to a distant location within 1 mile, allowing you to see and hear as if you were there for up to 10 minutes.", # Astral Projection
      "Gain a +2 status bonus to AC against attacks made by summoned or incorporeal creatures.", # Occult Defense
      "Inscribe a special sigil on an item or location, granting a +1 status bonus to defenses or saves against a specific school of magic." # Sigil Mastery
   ],
   'atf_cost' : [
      3, 2, 3, 2, 2, 2, 2, 3, 2, 3, 2, 3, 3, 3, 2
   ]
}

paladin_atfoptions = {
   'atf_name' : [
      "Retributive Strike",
      "Divine Grace",
      "Aura of Courage",
      "Righteous Smite",
      "Divine Ally",
      "Holy Shield",
      "Champion's Reaction",
      "Aura of Justice",
      "Blade of Justice",
      "Divine Health",
      "Smite Evil",
      "Shield of Faith",
      "Vengeful Oath",
      "Hero's Defiance",
      "Aura of Faith"
   ],
   'atf_info' : [
      "Reaction to reduce damage by 2 + your level against an adjacent ally and make a melee Strike against the attacker.", # Retributive Strike
      "Gain a +2 circumstance bonus to saving throws against spells and magical effects for 1 round.", # Divine Grace
      "Allies within 10 feet gain a +1 status bonus to saving throws against fear effects.", # Aura of Courage
      "Once per day, add d6 equal to total of dice rolled persistent sanctified damage to your next melee Strike.", # Righteous Smite
      "Choose a divine ally, such as a weapon, shield, or mount, gaining specific benefits based on the choice.", # Divine Ally
      "Once per day, raise your shield as a reaction to gain a +2 circumstance bonus to AC against an attack.", # Holy Shield
      "As a reaction, protect an ally within 15 feet, granting them a +2 circumstance bonus to AC against one attack.", # Champion's Reaction
      "Allies within 10 feet gain the benefits of your Retributive Strike, allowing them to deal an additional 1d6 damage on a hit.", # Aura of Justice
      "Deal an extra d6 equal to total of dice rolled damage on your first attack each round against a non-humanoid.", # Blade of Justice
      "Gain immunity to all diseases, including supernatural and magical diseases.", # Divine Health
      "Once per day, deal an additional d6 equal to total of dice rolled damage against a humanoid with a melee Strike.", # Smite Evil
      "Gain a +2 status bonus to AC for 1 minute, usable once per day.", # Shield of Faith
      "When you swear an oath against an enemy, gain a +2 circumstance bonus to attack rolls against that enemy until it is defeated.", # Vengeful Oath
      "Once per day, if you are reduced to 0 Hit Points, you can instead drop to 1 Hit Point and immediately heal 2d8 Hit Points.", # Hero's Defiance
      "Allies within 10 feet gain resistance 5 to all damage." # Aura of Faith
   ],
   'atf_cost' : [
      3, 2, 2, 3, 3, 2, 3, 3, 3, 2, 3, 2, 3, 3, 3
   ]
}

pugilist_atfoptions = {
   'atf_name' : [
      "Iron Fist",
      "Knockout Blow",
      "Counterpunch",
      "Body Blow",
      "Flurry of Blows",
      "Stunning Fist",
      "Grapple Master",
      "Haymaker",
      "Tough as Nails",
      "Deflect Strike",
      "Crushing Grip",
      "Quick Jab",
      "Ki Strike",
      "Endure Pain",
      "Brutal Beatdown"
   ],
   'atf_info' : [
      "Your unarmed strikes deal 1d6 bludgeoning damage and have the forceful trait.", # Iron Fist
      "Once per day, attempt a melee Strike; if you hit, the target must succeed on a Fortitude save or be stunned 1.", # Knockout Blow
      "Reaction to make an unarmed Strike against a creature that critically misses you with a melee attack.", # Counterpunch
      "On a successful hit with an unarmed Strike, the target must succeed on a Fortitude save or be sickened 1.", # Body Blow
      "Make two unarmed Strikes as a single action; if both hit, combine their damage for overcoming resistances.", # Flurry of Blows
      "On a critical hit with an unarmed Strike, the target must succeed on a Fortitude save or be stunned 1.", # Stunning Fist
      "Gain a +1 circumstance bonus to Athletics checks to Grapple and a +2 circumstance bonus to maintain a Grapple.", # Grapple Master
      "Make an unarmed Strike with a -2 penalty; if it hits, add an additional damage die.", # Haymaker
      "Gain a +1 circumstance bonus to Fortitude saves and resistance 2 to physical damage.", # Tough as Nails
      "Reaction to reduce damage from a melee attack by an amount equal to your level.", # Deflect Strike
      "When you successfully Grapple a creature, it takes 1d6 bludgeoning damage at the start of each of its turns while Grappled.", # Crushing Grip
      "Gain a +2 circumstance bonus to initiative checks and your first unarmed Strike in combat gains a +1 circumstance bonus to attack rolls.", # Quick Jab
      "Once per day, add 1d6 force damage to your unarmed Strike.", # Ki Strike
      "Gain temporary Hit Points equal to 5 + your level when you drop to 25% or less of your maximum Hit Points.", # Endure Pain
      "When you critically hit with an unarmed Strike, the target is flat-footed until the start of your next turn." # Brutal Beatdown
   ],
   'atf_cost' : [
      2, 3, 3, 3, 3, 3, 2, 2, 2, 3, 3, 2, 3, 2, 3
   ]
}

shaman_atfoptions = {
   'atf_name' : [
      "Spirit Bond",
      "Totemic Invocation",
      "Ritual Caster",
      "Spirit Animal",
      "Ancestral Guidance",
      "Elemental Ward",
      "Hex Mastery",
      "Spirit Step",
      "Fetish Crafter",
      "Spirit Strike",
      "Totemic Transformation",
      "Spirit Link",
      "Cleansing Ritual",
      "Ward of the Ancestors",
      "Empower Spirits"
   ],
   'atf_info' : [
      "Form a bond with a spirit, gaining a +1 status bonus to skill checks related to that spirit's domain (e.g., nature, healing).", # Spirit Bond
      "Once per day, invoke a totem spirit to gain a +2 circumstance bonus to attack rolls or saving throws for 1 minute.", # Totemic Invocation
      "Gain the ability to perform specific rituals related to the spirits you commune with, with a +2 circumstance bonus to the ritual skill check.", # Ritual Caster
      "Gain an animal companion that gains the spirit trait and a +1 circumstance bonus to Perception checks.", # Spirit Animal
      "Once per day, call upon your ancestors to gain a +2 status bonus to a skill check or attack roll.", # Ancestral Guidance
      "Gain resistance 5 to a specific type of elemental damage (fire, cold, lightning, or acid) for 1 hour.", # Elemental Ward
      "Learn a hex that allows you to impose a -1 status penalty on a target’s attack rolls or saving throws for 1 minute (once per day).", # Hex Mastery
      "Once per day, teleport 30 feet to an unoccupied space you can see as a free action.", # Spirit Step
      "Craft a magical fetish that grants a +1 circumstance bonus to saves against fear effects when carried.", # Fetish Crafter
      "Once per day, add 1d6 force damage to a melee or ranged attack.", # Spirit Strike
      "Assume the form of your totem spirit, gaining abilities based on the chosen animal (e.g., flight, swim speed) for 1 minute.", # Totemic Transformation
      "Share damage with an ally within 30 feet, reducing their damage by half and taking the other half yourself (up to a maximum of 10 damage).", # Spirit Link
      "Perform a cleansing ritual that removes one condition or curse from yourself or an ally once per day.", # Cleansing Ritual
      "Gain a +2 circumstance bonus to AC for 1 minute, usable once per day.", # Ward of the Ancestors
      "Your spirit animal or totem spirit gains a +1 status bonus to attacks and damage rolls for 1 minute, usable once per day." # Empower Spirits
   ],
   'atf_cost' : [
      2, 3, 2, 3, 2, 2, 3, 3, 2, 3, 4, 3, 3, 3, 3
   ]
}

soldier_atfoptions = {
   'atf_name' : [
      "Tactical Strike",
      "Armor Training",
      "Battlefield Awareness",
      "Weapon Specialization",
      "Shield Wall",
      "Combat Reflexes",
      "Brutal Assault",
      "Coordinated Attack",
      "Fortified Stance",
      "Battle Cry",
      "Defensive Tactics",
      "Weapon Mastery",
      "Hold the Line",
      "Unyielding Advance",
      "Veteran's Resolve"
   ],
   'atf_info' : [
      "Gain a +1 circumstance bonus to attack rolls when an ally is adjacent to your target.", # Tactical Strike
      "Reduce the armor check penalty and increase the maximum Dexterity bonus of worn armor by 1.", # Armor Training
      "Gain a +2 circumstance bonus to Perception checks to avoid being surprised.", # Battlefield Awareness
      "Gain a +2 bonus to damage rolls with your chosen weapon.", # Weapon Specialization
      "When adjacent to an ally with a shield, gain a +2 circumstance bonus to AC.", # Shield Wall
      "Gain an additional reaction each round, usable only for Attacks of Opportunity.", # Combat Reflexes
      "When you hit a creature with a melee weapon, it takes an additional 1d6 damage.", # Brutal Assault
      "When you and an ally attack the same target in the same round, both gain a +1 circumstance bonus to damage rolls.", # Coordinated Attack
      "Gain a +2 circumstance bonus to saves against effects that would move you or knock you prone.", # Fortified Stance
      "When you roll initiative, you can Demoralize a foe within 30 feet as a free action.", # Battle Cry
      "Gain a +1 circumstance bonus to AC against attacks of opportunity.", # Defensive Tactics
      "Choose a weapon group; gain a +1 circumstance bonus to attack rolls with all weapons in that group.", # Weapon Mastery
      "Gain a +1 circumstance bonus to attack rolls and damage when using the Ready action to make an attack.", # Hold the Line
      "As an action, move up to half your speed towards an enemy without triggering reactions.", # Unyielding Advance
      "Once per day, gain temporary Hit Points equal to 10 + your level when reduced to 0 Hit Points." # Veteran's Resolve
   ],
   'atf_cost' : [
      2, 2, 2, 3, 3, 3, 3, 2, 2, 2, 2, 3, 2, 3, 3
   ]
}

sorcerer_atfoptions = {
   'atf_name' : [
      "Metamagic Mastery",
      "Arcane Insight",
      "Spell Penetration",
      "Magical Adept",
      "Arcane Reflexes",
      "Blood Magic",
      "Heightened Casting",
      "Mystic Counter",
      "Esoteric Knowledge",
      "Quickened Casting",
      "Spell Substitution",
      "Arcane Defense",
      "Innate Magic",
      "Energy Absorption",
      "Spell Perfection"
   ],
   'atf_info' : [
      "Once per day, apply a metamagic feat to a spell without increasing its casting time.", # Metamagic Mastery
      "Gain a +1 bonus to Arcana checks and a +1 circumstance bonus to spell DCs against identified creatures.", # Arcane Insight
      "Gain a +2 bonus on checks to overcome spell resistance.", # Spell Penetration
      "Learn one additional cantrip from the arcane spell list.", # Magical Adept
      "Cast a cantrip as a reaction once per round.", # Arcane Reflexes
      "When casting a spell, gain temporary Hit Points equal to the spell's level.", # Blood Magic
      "Once per day, heighten a spell to a higher level without using a higher-level spell slot.", # Heightened Casting
      "Use your reaction to counter a spell by expending a spell slot of the same or higher level.", # Mystic Counter
      "Gain a +2 circumstance bonus to Arcana, Occultism, or Religion checks.", # Esoteric Knowledge
      "Once per day, cast a spell of up to 3rd level as a free action.", # Quickened Casting
      "Replace one of your prepared spells with another spell from your known spells once per day.", # Spell Substitution
      "Gain a +1 circumstance bonus to saving throws against spells and magical effects.", # Arcane Defense
      "Cast an additional 1st-level spell from your known spells once per day without using a spell slot.", # Innate Magic
      "Gain resistance 5 to a chosen energy type (fire, cold, electricity, or acid) for 1 hour, once per day.", # Energy Absorption
      "Choose one spell you know; you cast it with a +2 circumstance bonus to attack rolls and spell DCs." # Spell Perfection
   ],
   'atf_cost' : [
      3, 2, 3, 2, 3, 3, 3, 3, 2, 3, 2, 2, 2, 2, 3
   ]
}

thief_atfoptions = {
   'atf_name' : [
      "Sneak Attack",
      "Evasion",
      "Trap Finder",
      "Quick Disarm",
      "Nimble Dodge",
      "Uncanny Dodge",
      "Finesse Striker",
      "Dastardly Trick",
      "Hide in Plain Sight",
      "Opportunist",
      "Improved Initiative",
      "Shadow Striker",
      "Slippery Mind",
      "Ambush Master",
      "Quick Stealth"
   ],
   'atf_info' : [
      "Deal an additional d6 equal to total of dice rolled precision damage to flat-footed or flanked enemies.", # Sneak Attack
      "When you succeed at a Reflex save against an area effect, take no damage instead of half.", # Evasion
      "Gain a +1 bonus to Perception and Thievery checks to locate and disable traps.", # Trap Finder
      "Gain a +2 circumstance bonus to disarm attempts and disarm as a single action.", # Quick Disarm
      "Use a reaction to gain a +2 circumstance bonus to AC against one attack.", # Nimble Dodge
      "You cannot be flat-footed to hidden, undetected, or flanking creatures.", # Uncanny Dodge
      "Add your Dexterity modifier instead of Strength to damage rolls with finesse weapons.", # Finesse Striker
      "Once per round, attempt to Feint as a free action.", # Dastardly Trick
      "Hide even while being observed, as long as you are in dim light or darkness.", # Hide in Plain Sight
      "Make an attack of opportunity against a foe that is hit by another ally within reach.", # Opportunist
      "Gain a +2 circumstance bonus to initiative checks.", # Improved Initiative
      "Gain a +1 bonus to attack rolls when attacking from a hidden or concealed position.", # Shadow Striker
      "Gain a +2 circumstance bonus to saving throws against mental effects.", # Slippery Mind
      "Gain a +2 circumstance bonus to attack rolls when attacking a creature that has not yet acted in combat.", # Ambush Master
      "Move at full speed while using the Stealth skill without penalty." # Quick Stealth
   ],
   'atf_cost' : [
      1, 3, 1, 2, 2, 3, 3, 2, 3, 3, 2, 2, 2, 3, 2
   ]
}

wanderer_atfoptions = {
   'atf_name' : [
      "Wanderer's Step",
      "Survivalist",
      "Trailblazer",
      "Unfettered Movement",
      "Eyes of the Wild",
      "Forager's Instinct",
      "Endurance",
      "Seasoned Traveler",
      "Wayfinder",
      "Nomadic Resilience",
      "Wilderness Medicine",
      "Terrain Mastery",
      "Pathfinder",
      "Adaptable Tactics",
      "Endless Journey"
   ],
   'atf_info' : [
      "Gain a +10-foot bonus to your movement speed when traveling in the wilderness.", # Wanderer's Step
      "Gain a +1 bonus to Survival checks and treat natural difficult terrain as normal terrain.", # Survivalist
      "You and allies within 30 feet move through natural difficult terrain at full speed.", # Trailblazer
      "You cannot be slowed by difficult terrain caused by natural environments.", # Unfettered Movement
      "Gain low-light vision or darkvision (if you already have low-light vision) when in natural environments.", # Eyes of the Wild
      "Gain a +2 circumstance bonus to checks made to find food, water, or shelter in the wilderness.", # Forager's Instinct
      "Gain a +2 circumstance bonus to saves against fatigue and exhaustion effects.", # Endurance
      "You automatically know the direction of true north and cannot get lost in natural environments.", # Seasoned Traveler
      "Gain a +1 circumstance bonus to checks made to recall knowledge about geography or terrain.", # Wayfinder
      "Once per day, recover 1d8 Hit Points after resting for 10 minutes in a natural environment.", # Nomadic Resilience
      "Gain a +2 circumstance bonus to Medicine checks when treating wounds in the wilderness.", # Wilderness Medicine
      "Gain a +1 bonus to attack rolls and AC when fighting in a specific type of terrain (forest, desert, etc.).", # Terrain Mastery
      "Gain a +2 circumstance bonus to Perception checks to spot hidden or concealed creatures in natural environments.", # Pathfinder
      "Once per day, change your chosen terrain for the Terrain Mastery feat after resting for 10 minutes.", # Adaptable Tactics
      "Gain a +1 circumstance bonus to Fortitude saves against environmental hazards and extended travel fatigue." # Endless Journey
   ],
   'atf_cost' : [
      2, 2, 3, 3, 2, 2, 1, 2, 1, 2, 2, 3, 2, 2, 1
   ]
}

wizard_atfoptions = {
   'atf_name' : [
      "Arcane School",
      "Spellbook Prodigy",
      "Cantrip Expansion",
      "Arcane Bond",
      "Metamagic Expert",
      "Counterspell",
      "Spell Mastery",
      "Spell Recall",
      "Quickened Casting",
      "Enhanced Familiar",
      "Warding Ritual",
      "Arcane Thesis",
      "Heightened Spell",
      "Spell Substitution",
      "Arcane Sight"
   ],
   'atf_info' : [
      "Gain a +1 bonus to spell attack rolls and DCs with spells from your chosen school of magic.", # Arcane School
      "Add two additional spells to your spellbook at each level, instead of one.", # Spellbook Prodigy
      "Learn two additional cantrips from the arcane spell list.", # Cantrip Expansion
      "Once per day, cast any spell you know without expending a spell slot.", # Arcane Bond
      "Reduce the spell level increase of metamagic feats by 1 (minimum +0).", # Metamagic Expert
      "Use your reaction to counter a spell by expending the same or higher-level spell slot.", # Counterspell
      "Choose one spell you know; you can prepare it once per day without expending a spell slot.", # Spell Mastery
      "Once per day, regain an expended spell slot of up to 5th level.", # Spell Recall
      "Once per day, cast a spell of up to 3rd level as a free action.", # Quickened Casting
      "Your familiar gains an additional familiar ability from the list of familiar abilities.", # Enhanced Familiar
      "Cast a ritual that provides a +1 circumstance bonus to AC for you and your allies for 1 hour.", # Warding Ritual
      "Gain a +2 bonus to spell DCs for a specific school of magic of your choice.", # Arcane Thesis
      "Once per day, cast a spell using a higher-level spell slot without altering its effects.", # Heightened Spell
      "Swap one prepared spell with another of the same level from your spellbook once per day.", # Spell Substitution
      "Detect magical auras within 30 feet as if using detect magic at will." # Arcane Sight
   ],
   'atf_cost' : [
      3, 2, 2, 4, 3, 3, 3, 4, 3, 2, 2, 3, 3, 2, 2
   ]
}

universal_atfoptions = {
   'atf_name' : [
      "Toughness",
      "Combat Reflexes",
      "Quick Recovery",
      "Skill Focus",
      "Weapon Focus",
      "Iron Will",
      "Great Fortitude",
      "Lightning Reflexes",
      "Improved Initiative",
      "Diehard",
      "Fleet",
      "Acrobatic Dodge",
      "Endurance",
      "Alertness",
      "Power Attack"
   ],
   'atf_info' : [
      "Gain an additional 3 Hit Points per level.", # Toughness
      "Gain an additional reaction each round, usable only for Attacks of Opportunity.", # Combat Reflexes
      "Reduce the time to recover from the fatigued, sickened, or frightened condition by half.", # Quick Recovery
      "Gain a +2 bonus to a chosen skill (e.g., Athletics, Perception).", # Skill Focus
      "Gain a +1 bonus to attack rolls with a chosen weapon.", # Weapon Focus
      "Gain a +2 bonus on Will saving throws.", # Iron Will
      "Gain a +2 bonus on Fortitude saving throws.", # Great Fortitude
      "Gain a +2 bonus on Reflex saving throws.", # Lightning Reflexes
      "Gain a +2 bonus to initiative checks.", # Improved Initiative
      "When reduced to 0 Hit Points, you do not fall unconscious and can continue acting until you reach negative Hit Points equal to your Constitution score.", # Diehard
      "Increase your base land speed by 5 feet.", # Fleet
      "Gain a +2 circumstance bonus to AC against attacks made while you are moving through threatened areas.", # Acrobatic Dodge
      "Gain a +2 bonus on checks to resist nonlethal damage, environmental effects, and exhaustion.", # Endurance
      "Gain a +2 bonus on Perception checks and to initiative when you are not surprised.", # Alertness
      "Make a single melee Strike with a -2 penalty to the attack roll to deal an additional weapon damage die." # Power Attack
   ],
    'atf_cost' : [
      2, 3, 2, 1, 2, 2, 2, 2, 2, 3, 2, 2, 1, 2, 3
   ]
}

rare_atfoptions = {
   'atf_name' : [
      "Draconic Breath",
      "Giant's Strength",
      "Vampiric Touch",
      "Werewolf Transformation",
      "Lich's Resilience",
      "Stone Giant's Endurance",
      "Infernal Pact",
      "Dragon's Scales",
      "Shadow Step",
      "Elemental Fury",
      "Ghoul's Paralyze",
      "Phoenix Rebirth",
      "Storm Giant's Thunder",
      "Troll Regeneration",
      "Mind Flayer's Psionics"
   ],
   'atf_info' : [
      "Once per day, exhale a cone of elemental energy (fire, cold, acid, or lightning) dealing 6d6 damage; Reflex save for half.", # Draconic Breath
      "Gain a +4 bonus to Strength checks and Strength-based skill checks for 1 minute, once per day.", # Giant's Strength
      "Once per day, make a melee touch attack to drain 1d6 Hit Points from a target and heal yourself for the same amount.", # Vampiric Touch
      "Once per day, transform into a hybrid werewolf form for 1 minute, gaining a +2 bonus to attack and damage rolls, and a +10-foot bonus to movement speed.", # Werewolf Transformation
      "Gain resistance 10 to cold and negative energy, and a +2 bonus to saves against death effects.", # Lich's Resilience
      "Gain resistance 5 to physical damage and a +2 bonus to Fortitude saves for 1 minute, once per day.", # Stone Giant's Endurance
      "Once per day, gain a +2 bonus to Charisma-based checks and fire resistance 10 for 1 hour.", # Infernal Pact
      "Gain a +2 natural armor bonus to AC and resistance 5 to the energy type associated with a dragon's breath (fire, cold, acid, lightning).", # Dragon's Scales
      "Once per day, teleport up to 30 feet to a shadowy or dimly lit area as a free action.", # Shadow Step
      "Once per day, enter a state of elemental fury, adding 1d6 elemental damage (fire, cold, acid, or lightning) to your melee attacks for 1 minute.", # Elemental Fury
      "Once per day, make a melee touch attack to paralyze a target for 1d4 rounds unless it succeeds on a Fortitude save.", # Ghoul's Paralyze
      "Once per day, when reduced to 0 Hit Points, instantly heal for 5d6 Hit Points and surround yourself with a fiery aura that deals 2d6 fire damage to creatures within 10 feet.", # Phoenix Rebirth
      "Once per day, call down a bolt of lightning as a ranged touch attack, dealing 4d6 lightning damage and deafening the target for 1 round.", # Storm Giant's Thunder
      "Gain regeneration 5 for 1 minute, which stops functioning if you take acid or fire damage, usable once per day.", # Troll Regeneration
      "Once per day, use telepathy to communicate with any creature within 60 feet, and cast mind-affecting spells as if you had the Psionic subtype." # Mind Flayer's Psionics
   ],
   'atf_cost' : [
      4, 3, 3, 4, 3, 3, 2, 4, 3, 3, 4, 4, 3, 4, 4
   ],
}
