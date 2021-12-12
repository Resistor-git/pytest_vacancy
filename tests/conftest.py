import pytest
import shutil
import sqlite3

from pathlib import Path
from random import randint


@pytest.fixture(scope='session')
def copy_db():
    """returns path for copy of the database"""
    # looks for wargaming.db in parent directory of test_random_changes.py
    path = Path('.')
    DATABASE_PATH = path / 'wargaming.db'
    # makes copy of wargaming.db
    # db_copy_for_tst is a string - path to the file (?)
    db_copy_for_tst = shutil.copyfile(DATABASE_PATH, 'tests\\db_copy_for_tst.db')
    return db_copy_for_tst
    

# I don't actually understand how 'autouse=True' works. But without it the function doesn't execute.
@pytest.fixture(autouse=True)
def change_ships_properties(copy_db):
    """changes columns weapon, hull, engine in Ships table;
    takes the result of copy_db() and makes random changes in it
    'Для каждого корабля меняется на случайный один из компонентов: корпус, орудие или двигатель'
    """
    # print("\nMYDEBUG", copy_db)
    # print("\nMYDEBUG", type(copy_db))
    con = sqlite3.connect(copy_db)
    cur = con.cursor()

    # list with each ship
    list_of_ships = []
    for i in range(1, 201):
        ship = "ship-" + str(i)
        # print(ship)
        list_of_ships.append(ship)

    # each list contains ships with changed properties, one list per property [('weapon-19', 'ship-1'), ('weapon-5', 'ship-22', )...]; [('hull-3', 'ship-4'), ('hull-5', 'ship-7', )...]
    list_of_weapon_changes = []
    list_of_hull_changes = []
    list_of_engine_changes = []

    # change either weapon or hull or engine of each ship, based on random_number
    for ship in list_of_ships:
        random_number = randint(1, 3)
        if random_number == 1:
            # change weapon
            print(f"\nrandom_number = {random_number}, changing weapon in Ships table for {ship}")
            new_weapon = "weapon-" + str(randint(1, 20))
            list_of_weapon_changes.append((new_weapon, ship))
        elif random_number == 2:
            # change hull
            print(f"\nrandom_number = {random_number}, changing hull in Ships table for {ship}")
            new_hull = "hull-" + str(randint(1, 20))
            list_of_hull_changes.append((new_hull, ship))
        elif random_number == 3:
            # change engine
            print(f"\nrandom_number = {random_number}, changing engine in Ships table for {ship}")
            new_engine = "engine-" + str(randint(1, 20))
            list_of_engine_changes.append((new_engine, ship))
    # print(list_of_weapon_changes)
    # print(list_of_hull_changes)
    # print(list_of_engine_changes)
    
    # write changed weapon in Ships table
    with con:
        cur.executemany(f"UPDATE Ships SET weapon = ? WHERE ship = ?", list_of_weapon_changes)
    # write changed hull in Ships table
    with con:
        cur.executemany(f"UPDATE Ships SET hull = ? WHERE ship = ?", list_of_hull_changes)
    # write changed engine in Ships table
    with con:
        cur.executemany(f"UPDATE Ships SET engine = ? WHERE ship = ?", list_of_engine_changes)