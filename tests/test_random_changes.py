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

    # 200 random weapon parameters (one per each ship)
    # list_of_weapons = []
    
    rand_numbers_weapon = [randint(1, 20) for num in range(200)]

    # for i in range(1, 201):
    #     weapon = "weapon-" + str(randint(1, 20))
    #     list_of_weapons.append(weapon)
    # print("!!!!!", list_of_weapons)

    # # cur.executemany expects list of tuples as a wildcard
    # rand_numbers_tuples_weapon = [(num,) for num in rand_numbers_weapon]
    #print(rand_numbers_tuples_weapon)

    list_of_ships = []
    for i in range(1, 201):
        ship = "ship-" + str(i)
        # print(ship)
        list_of_ships.append(ship)
    # cur.executemany expects list of tuples as a wildcard (does it?)
    # ship_weapon_tuple consists of tuples ('ship-x', number)
    ship_weapon_tuple = tuple(zip(rand_numbers_weapon, list_of_ships))
    #print(ship_weapon_tuple)

    with con:
        # randomize weapon for each ship (each row in table Ships)
        cur.executemany("UPDATE Ships SET weapon = ? WHERE ship = ?", ship_weapon_tuple)
    assert 1 == 1

