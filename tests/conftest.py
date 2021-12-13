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
@pytest.fixture()
def original_db():
    """returns path for original database"""
    # looks for wargaming.db in parent directory of test_random_changes.py
    path = Path('.')
    DATABASE_PATH = path / 'wargaming.db'
    # makes copy of wargaming.db
    return DATABASE_PATH
    

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
    # print("list_of_weapon_changes", list_of_weapon_changes)
    # print("list_of_hull_changes", list_of_hull_changes)
    # print("list_of_engine_changes",list_of_engine_changes)
    
    # write changed weapon in Ships table
    with con:
        cur.executemany(f"UPDATE Ships SET weapon = ? WHERE ship = ?", list_of_weapon_changes)
    # write changed hull in Ships table
    with con:
        cur.executemany(f"UPDATE Ships SET hull = ? WHERE ship = ?", list_of_hull_changes)
    # write changed engine in Ships table
    with con:
        cur.executemany(f"UPDATE Ships SET engine = ? WHERE ship = ?", list_of_engine_changes)


# may be buggy; does it take the original copy or copy modified by test_change_ships_properties ???
# I don't actually understand how 'autouse=True' works. But without it the function doesn't execute.
@pytest.fixture(autouse=True)
def change_weapons_hulls_engines_properties(copy_db):
    """takes the result of copy_db() and makes random change in random property for each row of tables Weapons, Hulls, Engines
    'В каждом компоненте меняется один из случайно выбранных параметров на случайное значение из допустимого диапазона'
    """
    con = sqlite3.connect(copy_db)
    cur = con.cursor()
  
    # change columns in Weapons table
    print("\nchanging properties in Weapons table")
    # attmept to make code a little more flexible, without hardcoded number of rows
    # fetchall() returns a list of tuples, like [(15,)]
    quantity_of_rows_weapons = cur.execute("SELECT COUNT(*) FROM Weapons").fetchall()[0][0]

    for i in range(1, quantity_of_rows_weapons + 1):
        # "weapon" is used as a pointer in table, to show cur.execute which row should be changed
        weapon = "weapon-" + str(i)
        # max n = number of columns which can be changed (only one of them will be changed)
        n = randint(1, 6)
        if n == 1:
            print(f"\nn = {n}, changing reload_speed in Weapons table for {weapon}")
            with con:
                cur.execute("UPDATE Weapons SET reload_speed = :reload_speed WHERE weapon = :weapon", {"reload_speed" : randint(1, 20), "weapon" : weapon})
        elif n == 2:
            print(f"\nn = {n}, changing rotation_speed in Weapons table for {weapon}")
            with con:
                cur.execute("UPDATE Weapons SET rotation_speed = :rotation_speed WHERE weapon = :weapon", {"rotation_speed" : randint(1, 20), "weapon" : weapon})
        elif n == 3:
            print(f"\nn = {n}, changing diameter in Weapons table for {weapon}")
            with con:
                cur.execute("UPDATE Weapons SET diameter = :diameter WHERE weapon = :weapon", {"diameter" : randint(1, 20), "weapon" : weapon})
        elif n == 4:
            print(f"\nn = {n}, changing power_volley in Weapons table for {weapon}")
            with con:
                cur.execute("UPDATE Weapons SET power_volley = :power_volley WHERE weapon = :weapon", {"power_volley" : randint(1, 20), "weapon" : weapon})
        elif n == 5:
            print(f"\nn = {n}, changing count in Weapons table for {weapon}")
            with con:
                cur.execute("UPDATE Weapons SET count = :count WHERE weapon = :weapon", {"count" : randint(1, 20), "weapon" : weapon})
    
    # change Hulls table
    print("\nchanging properties in Hulls table")
    # attmept to make code a little more flexible, without hardcoded number of rows
    # fetchall() returns a list of tuples, like [(15,)]
    quantity_of_rows_hulls = cur.execute("SELECT COUNT(*) FROM Hulls").fetchall()[0][0]

    for i in range(1, quantity_of_rows_hulls + 1):
        # "hull" is used as a pointer in table, to show cur.execute which row should be changed
        # max "n" = number of columns which can be changed (only one of them will be changed)
        hull = "hull-" + str(i)
        n = randint(1, 3)
        if n == 1:
            print(f"\nn = {n}, changing armor in Hulls table for {hull}")
            with con:
                cur.execute("UPDATE Hulls SET armor = :armor WHERE hull = :hull", {"armor" : randint(1, 20), "hull" : hull})
        elif n == 2:
            print(f"\nn = {n}, changing type in Hulls table for {hull}")
            with con:
                cur.execute("UPDATE Hulls SET type = :type WHERE hull = :hull", {"type" : randint(1, 20), "hull" : hull})
        elif n == 3:
            print(f"\nn = {n}, changing capacity in Hulls table for {hull}")
            with con:
                cur.execute("UPDATE Hulls SET capacity = :capacity WHERE hull = :hull", {"capacity" : randint(1, 20), "hull" : hull})
    
    # change Engines table
    print("\n changing properties in Engines table")
    # attmept to make code a little more flexible, without hardcoded number of rows
    # fetchall() returns a list of tuples, like [(15,)]
    quantity_of_rows_engines = cur.execute("SELECT COUNT(*) FROM Engines").fetchall()[0][0]

    for i in range(1, quantity_of_rows_engines + 1):
        # "engine" is used as a pointer in table, to show cur.execute which row should be changed
        # max "n" = number of columns which can be changed (only one of them will be changed)
        engine = "engine-" + str(i)
        n = randint(1, 2)
        if n == 1:
            print(f"\nn = {n}, changing power in Engines table for {engine}")
            with con:
                cur.execute("UPDATE Engines SET power = :power WHERE engine = :engine", {"power" : randint(1, 20), "engine" : engine})
        elif n == 2:
            print(f"\nn = {n}, changing type in Engines table for {engine}")
            with con:
                cur.execute("UPDATE Engines SET type = :type WHERE engine = :engine", {"type" : randint(1, 20), "engine" : engine})



@pytest.fixture()
def what_changed_in_ships(copy_db, original_db):
    """Checks if weapon or hull or engine was changed for each ship in table Ships"""
    # connection to original database
    con_orig = sqlite3.connect(original_db)
    cur_orig = con_orig.cursor()

    data_orig = cur_orig.execute("SELECT * FROM Ships").fetchall()
    # print("original", data_orig)

    # connection to temporary copy with changes
    con_temp = sqlite3.connect(copy_db)
    cur_temp = con_temp.cursor()

    data_copy = cur_temp.execute("SELECT * FROM Ships").fetchall()
    # print("copy:", data_copy)

    # create list with all differences between original and modified databases
    # differences is a list of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
    i = 0
    differences = []
    for row in data_orig:
        differences.append((data_orig[i], data_copy[i]))
        i += 1
    # print(differences)

    for difference in differences:
        # difference is tuple of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
        print(difference)
        # print('original', difference[0])
        # print('copy', difference[1])
        # compare each element of tuple to another element of tuple, in other words compare every property of ship from original db with every property of ship from temporary db
        for n in range(0, len(differences[0][0])):
            if difference[0][n] != difference[1][n]:
                # Ship-x, property-y (data from temp db)
                #   expected property-z (from original db), was property-y (from temp db)

                # difference[0] - original, difference[1] - temporary
                print(f"""{difference[1][0]}, {difference[1][n]}\n    expected {difference[0][n]}, was {difference[1][n]}""")
                yield difference