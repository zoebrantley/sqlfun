TOTAL_CHARACTERS = '''SELECT COUNT(*) FROM charactercreator_character;'''

DISTINCT_CHARACTER_NAMES = '''
    SELECT COUNT(DISTINCT name) AS distinct_names
    FROM charactercreator_character;
'''

TOTAL_NECRO = '''SELECT COUNT(*) FROM charactercreator_necromancer;'''

TOTAL_ARMORY_ITEMS = '''SELECT COUNT(*) FROM armory_item;'''

TOTAL_WEAPONS = '''SELECT COUNT(*) 
    FROM armory_weapon AS AW
    INNER JOIN armory_item as AI
    WHERE AI.item_id = AW.item_ptr_id;
'''

ALL_WEAPONS_INFO = '''
    SELECT * 
    FROM armory_weapon AS AW
    INNER JOIN armory_item as AI
    WHERE AI.item_id = AW.item_ptr_id;
'''

TOTAL_NON_WEAPONS = '''SELECT COUNT(*) 
    FROM armory_item AS AI
    LEFT JOIN armory_weapon as AW
    ON AI.item_id = AW.item_ptr_id
    WHERE AW.power IS NULL;
'''

ITEMS_PER_CHAR = '''SELECT name, COUNT(item_id) 
    FROM charactercreator_character AS CC
    INNER JOIN charactercreator_character_inventory as INV
    ON CC.character_id = INV.character_id
    GROUP BY CC.character_id;
'''

WEAPONS_PER_CHAR = '''SELECT CC.name, COUNT(AI.item_id) AS total_weapons
    FROM armory_item as AI
    INNER JOIN armory_weapon as AW
    ON AI.item_id = AW.item_ptr_id
    INNER JOIN charactercreator_character_inventory as INV
    ON AI.item_id = INV.item_id
    INNER JOIN charactercreator_character AS CC
    ON CC.character_id = INV.character_id
    GROUP BY CC.character_id;
'''

AVG_CHAR_WEAPONS = '''SELECT AVG(total_weapons) AS avg_weapons
    FROM (SELECT CC.name, COUNT(AI.item_id) AS total_weapons
        FROM armory_item as AI
        INNER JOIN armory_weapon as AW
        ON AI.item_id = AW.item_ptr_id
        INNER JOIN charactercreator_character_inventory as INV
        ON AI.item_id = INV.item_id
        INNER JOIN charactercreator_character AS CC
        ON CC.character_id = INV.character_id
        GROUP BY CC.character_id);
        '''

AVG_CHAR_ITEMS = '''SELECT AVG(total_items) as avg_items
    FROM (SELECT name, COUNT(item_id) AS total_items 
        FROM charactercreator_character AS CC
        INNER JOIN charactercreator_character_inventory as INV
        ON CC.character_id = INV.character_id
        GROUP BY CC.character_id);
        '''

QUERY_LIST = [TOTAL_CHARACTERS, DISTINCT_CHARACTER_NAMES,
              TOTAL_NECRO, TOTAL_ARMORY_ITEMS,
              TOTAL_WEAPONS, ALL_WEAPONS_INFO,
              TOTAL_NON_WEAPONS, ITEMS_PER_CHAR,
              AVG_CHAR_WEAPONS, AVG_CHAR_ITEMS, WEAPONS_PER_CHAR]
