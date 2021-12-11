import shutil
import pytest
import sqlite3

from pathlib import Path
from random import randint

@pytest.fixture(scope='session')
def copy_db():
    # looks for wargaming.db in parent directory of test_random_changes.py
    path = Path('.')
    DATABASE_PATH = path / 'wargaming.db'
    # makes copy of wargaming.db
    # db_copy_for_tst is a string - path to the file (?)
    db_copy_for_tst = shutil.copyfile(DATABASE_PATH, 'tests\\db_copy_for_tst.db')
    return db_copy_for_tst


def test_change_weapon(copy_db):
    """takes the result of copy_db() and makes random changes in it"""
    # print("\nMYDEBUG", copy_db)
    # print("\nMYDEBUG", type(copy_db))
    con = sqlite3.connect(copy_db)
    cur = con.cursor()

    # change either weapon or hull or engine, based on random_number
    random_number = randint(1, 3)
    if random_number == 1:
        # change weapon
        print(f"\nrandom_number = {random_number}, changing weapon")

        # list with each ship
        list_of_ships = []
        for i in range(1, 201):
            ship = "ship-" + str(i)
            # print(ship)
            list_of_ships.append(ship)

        # 200 random weapon parameters (one per each ship)
        list_of_weapons = []
        for i in range(1, 201):
            weapon = "weapon-" + str(randint(1, 20))
            list_of_weapons.append(weapon)
        #print("!!!!!", list_of_weapons)

        # ship_weapon_tuple consists of tuples ('ship-x', number)
        # used for cur.executemany
        ship_weapon_tuple = list(zip(list_of_weapons, list_of_ships))
        # print(ship_weapon_tuple)

        # update randomized weapon for each ship (each row in table Ships)
        # cur.executemany expects ONE list (or tuple) of tuples as a wildcard, like ('weapon-5', 'ship-105')
        with con:
            cur.executemany("UPDATE Ships SET weapon = ? WHERE ship = ?", ship_weapon_tuple)
    elif random_number == 2:
        # change hull
        print(f"\nrandom_number = {random_number}, changing hull")

        list_of_ships = []
        for i in range(1, 201):
            ship = "ship-" + str(i)
            list_of_ships.append(ship)

        list_of_hulls = []
        for i in range(1, 201):
            hull = "hull-" + str(randint(1, 20))
            list_of_hulls.append(hull)

        ship_hull_tuple = list(zip(list_of_hulls, list_of_ships))
        #print(ship_hull_tuple)

        # update randomized hull for each ship (each row in table Ships)
        # cur.executemany expects ONE list (or tuple) of tuples as a wildcard, like ('hull-5', 'ship-105')
        with con:
            cur.executemany("UPDATE Ships SET hull = ? WHERE ship = ?", ship_hull_tuple)
    
    elif random_number == 3:
        # change engine
        print(f"\nrandom_number = {random_number}, changing engine")

        list_of_ships = []
        for i in range(1, 201):
            ship = "ship-" + str(i)
            list_of_ships.append(ship)

        list_of_engines = []
        for i in range(1, 201):
            hull = "engine-" + str(randint(1, 20))
            list_of_engines.append(hull)

        ship_engine_tuple = list(zip(list_of_engines, list_of_ships))
        #print(ship_hull_tuple)

        # update randomized engine for each ship (each row in table Ships)
        # cur.executemany expects ONE list (or tuple) of tuples as a wildcard, like ('engine-5', 'ship-105')
        with con:
            cur.executemany("UPDATE Ships SET engine = ? WHERE ship = ?", ship_engine_tuple)




    assert 1 == 1

