# COMMENTED PART DOES NOT WORK. IT GENERATES NEW TABLE, BUT RESULTS OF ASSERT ARE ALWAYS 'PASSED' AND NO PRINT OUTPUTS TO INDICATE THAT CODE ACTUALLY WORKS
import pytest
import shutil
import sqlite3

from pathlib import Path
from random import randint
from test_random_changes import FailMsg


#### generation of table with random changes
# @pytest.fixture(scope="session")
def pytest_sessionstart(session):
    """generates 'db_copy_for_tst.db' - copy of 'wargaming.db' but some values are replaced by other random values
    called after Session object is created, before collection, tests and everything else;
    appendix: this is not how task asked to do this, task asks to use @pytest.fixture(scope="session"), but in my case
    it doesn't work (can't call creation of db_copy_for_tst.db before pytest_generate_tests and can't call it inside
    because it either creates db_copy_for_tst.db several times or just tells that you can't call fixture this way"""
    print("""!!!!!!!!!!!!!!!!!!!!!!create_db_copy_for_tst started!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!""")
    # returns path for copy of the database
    # looks for wargaming.db in parent directory of test_random_changes.py
    path = Path('.')
    DATABASE_PATH_ORIG = path / 'wargaming.db'
    # makes copy of wargaming.db
    # db_copy_for_tst is a string - path to the file (?)
    db_copy_for_tst = shutil.copyfile(DATABASE_PATH_ORIG, 'tests\\db_copy_for_tst.db')

    """changes columns weapon, hull, engine in Ships table;
    takes the result of copy_db() and makes random changes in it
    'Для каждого корабля меняется на случайный один из компонентов: корпус, орудие или двигатель'
    """
    con_copy = sqlite3.connect(path / 'tests\\db_copy_for_tst.db')
    cur_copy = con_copy.cursor()

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
    with con_copy:
        cur_copy.executemany(f"UPDATE Ships SET weapon = ? WHERE ship = ?", list_of_weapon_changes)
    # write changed hull in Ships table
    with con_copy:
        cur_copy.executemany(f"UPDATE Ships SET hull = ? WHERE ship = ?", list_of_hull_changes)
    # write changed engine in Ships table
    with con_copy:
        cur_copy.executemany(f"UPDATE Ships SET engine = ? WHERE ship = ?", list_of_engine_changes)

        # may be buggy; does it take the original copy or copy modified by test_change_ships_properties ???
        """takes the result of copy_db() and makes random change in random property for each row of tables Weapons, Hulls, Engines
            'В каждом компоненте меняется один из случайно выбранных параметров на случайное значение из допустимого диапазона'
        """

        # change columns in Weapons table
        print("\nchanging properties in Weapons table")
        # attmept to make code a little more flexible, without hardcoded number of rows
        # fetchall() returns a list of tuples, like [(15,)]
        quantity_of_rows_weapons = cur_copy.execute("SELECT COUNT(*) FROM Weapons").fetchall()[0][0]

        for i in range(1, quantity_of_rows_weapons + 1):
            # "weapon" is used as a pointer in table, to show cur.execute which row should be changed
            weapon = "weapon-" + str(i)
            # max n = number of columns which can be changed (only one of them will be changed)
            n = randint(1, 6)
            if n == 1:
                print(f"\nn = {n}, changing reload_speed in Weapons table for {weapon}")
                with con_copy:
                    cur_copy.execute("UPDATE Weapons SET reload_speed = :reload_speed WHERE weapon = :weapon",
                                     {"reload_speed": randint(1, 20), "weapon": weapon})
            elif n == 2:
                print(f"\nn = {n}, changing rotation_speed in Weapons table for {weapon}")
                with con_copy:
                    cur_copy.execute("UPDATE Weapons SET rotation_speed = :rotation_speed WHERE weapon = :weapon",
                                     {"rotation_speed": randint(1, 20), "weapon": weapon})
            elif n == 3:
                print(f"\nn = {n}, changing diameter in Weapons table for {weapon}")
                with con_copy:
                    cur_copy.execute("UPDATE Weapons SET diameter = :diameter WHERE weapon = :weapon",
                                     {"diameter": randint(1, 20), "weapon": weapon})
            elif n == 4:
                print(f"\nn = {n}, changing power_volley in Weapons table for {weapon}")
                with con_copy:
                    cur_copy.execute("UPDATE Weapons SET power_volley = :power_volley WHERE weapon = :weapon",
                                     {"power_volley": randint(1, 20), "weapon": weapon})
            elif n == 5:
                print(f"\nn = {n}, changing count in Weapons table for {weapon}")
                with con_copy:
                    cur_copy.execute("UPDATE Weapons SET count = :count WHERE weapon = :weapon",
                                     {"count": randint(1, 20), "weapon": weapon})

        # change Hulls table
        print("\nchanging properties in Hulls table")
        # attempt to make code a little more flexible, without hardcoded number of rows
        # fetchall() returns a list of tuples, like [(15,)]
        quantity_of_rows_hulls = cur_copy.execute("SELECT COUNT(*) FROM Hulls").fetchall()[0][0]

        for i in range(1, quantity_of_rows_hulls + 1):
            # "hull" is used as a pointer in table, to show cur.execute which row should be changed
            # max "n" = number of columns which can be changed (only one of them will be changed)
            hull = "hull-" + str(i)
            n = randint(1, 3)
            if n == 1:
                print(f"\nn = {n}, changing armor in Hulls table for {hull}")
                with con_copy:
                    cur_copy.execute("UPDATE Hulls SET armor = :armor WHERE hull = :hull",
                                     {"armor": randint(1, 20), "hull": hull})
            elif n == 2:
                print(f"\nn = {n}, changing type in Hulls table for {hull}")
                with con_copy:
                    cur_copy.execute("UPDATE Hulls SET type = :type WHERE hull = :hull",
                                     {"type": randint(1, 20), "hull": hull})
            elif n == 3:
                print(f"\nn = {n}, changing capacity in Hulls table for {hull}")
                with con_copy:
                    cur_copy.execute("UPDATE Hulls SET capacity = :capacity WHERE hull = :hull",
                                     {"capacity": randint(1, 20), "hull": hull})

        # change Engines table
        print("\n changing properties in Engines table")
        # attmept to make code a little more flexible, without hardcoded number of rows
        # fetchall() returns a list of tuples, like [(15,)]
        quantity_of_rows_engines = cur_copy.execute("SELECT COUNT(*) FROM Engines").fetchall()[0][0]

        for i in range(1, quantity_of_rows_engines + 1):
            # "engine" is used as a pointer in table, to show cur.execute which row should be changed
            # max "n" = number of columns which can be changed (only one of them will be changed)
            engine = "engine-" + str(i)
            n = randint(1, 2)
            if n == 1:
                print(f"\nn = {n}, changing power in Engines table for {engine}")
                with con_copy:
                    cur_copy.execute("UPDATE Engines SET power = :power WHERE engine = :engine",
                                     {"power": randint(1, 20), "engine": engine})
            elif n == 2:
                print(f"\nn = {n}, changing type in Engines table for {engine}")
                with con_copy:
                    cur_copy.execute("UPDATE Engines SET type = :type WHERE engine = :engine",
                                     {"type": randint(1, 20), "engine": engine})


def pytest_generate_tests(metafunc):
    print("!!!!!!!!!!!!!!!!!!!!pytest_generate_tests started!!!!!!!!!!!!!!!!!!!!!", metafunc.function.__name__)
    """returns path for copy of the database"""
    # looks for wargaming.db in parent directory of test_random_changes.py
    path = Path('.')
    DATABASE_PATH_ORIG = path / 'wargaming.db'

    """changes columns weapon, hull, engine in Ships table;
    takes the result of copy_db() and makes random changes in it
    'Для каждого корабля меняется на случайный один из компонентов: корпус, орудие или двигатель'
    """
    # print("\nMYDEBUG", copy_db)
    # print("\nMYDEBUG", type(copy_db))
    con_copy = sqlite3.connect(path / 'tests\\db_copy_for_tst.db')
    cur_copy = con_copy.cursor()

    # connection to original database
    con_orig = sqlite3.connect(DATABASE_PATH_ORIG)
    cur_orig = con_orig.cursor()

    # generate data for "test_ships"
    if metafunc.function.__name__ == "test_ships":
        """Checks if weapon or hull or engine was changed for each ship in table Ships"""
        # # connection to original database
        # con_orig = sqlite3.connect(DATABASE_PATH_ORIG)
        # cur_orig = con_orig.cursor()

        data_orig = cur_orig.execute("SELECT * FROM Ships").fetchall()
        data_copy = cur_copy.execute("SELECT * FROM Ships").fetchall()

        # create list with all differences between original and modified databases
        # differences is a list of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
        i = 0
        differences = []
        for row in data_orig:
            differences.append((data_orig[i], data_copy[i]))
            i += 1

        con_orig.close()
        con_copy.close()
        metafunc.parametrize('orig, modif', differences)
    # generate data for test_ships_weapon
    elif metafunc.function.__name__ == "test_ships_weapon":
        """Checks if any weapons property changed for each weapon in table Weapons"""
        # connection to original database
        # con_orig = sqlite3.connect(DATABASE_PATH_ORIG)
        # cur_orig = con_orig.cursor()

        quantity_of_ships = cur_copy.execute("SELECT COUNT(*) FROM Ships").fetchall()[0][0]  # should be 200 by default
        # data_orig - list of tuples [(weapon-2, 4, 19, 18, 16, 14), (weapon-5, 7, 11, 6, 16, 9)...] no ship names
        data_orig = []
        for ship in range(quantity_of_ships + 1):
            print("ship:", ship)
            print(f'ship+ship: ship-{ship}')
            one_ship_weapon_data_orig = cur_orig.execute("""SELECT * FROM Weapons WHERE weapon IN
                                                        (SELECT weapon FROM Ships WHERE ship = :ship)""", {"ship": f"ship-{ship}"}).fetchall()
            # one_ship_weapon_data_orig.append(f'ship-{ship}')
            data_orig.append(one_ship_weapon_data_orig)
        print("!!!!data_orig!!!!!!", data_orig)

        data_copy = []
        for ship in range(quantity_of_ships + 1):
            one_ship_weapon_data_copy = cur_copy.execute("SELECT * FROM Weapons WHERE weapon IN (SELECT weapon FROM Ships WHERE ship = :ship)", {"ship": f"ship-{ship}"}).fetchall()
            data_copy.append(one_ship_weapon_data_copy)
        print("!!!!data_copy!!!!", data_copy)

        # create list with all differences between original and modified databases
        # differences is a list of tuples; each tuple looks like ((weapon-2, 7, 9, 8, 6, 9), (weapon-2, 7, 9, 8, 6, 14))
        i = 0
        differences = []
        for row in data_orig:
            differences.append((data_orig[i], data_copy[i]))
            i += 1
        con_orig.close()
        con_copy.close()
        metafunc.parametrize('orig, modif', differences)
    # generate data for test_ships_hull
    elif metafunc.function.__name__ == "test_ships_hull":
        """Checks if any hulls property changed for each hull in table Hulls"""
        # connection to original database
        # con_orig = sqlite3.connect(DATABASE_PATH_ORIG)
        # cur_orig = con_orig.cursor()

        data_orig = cur_orig.execute("SELECT * FROM Hulls").fetchall()
        data_copy = cur_copy.execute("SELECT * FROM Hulls").fetchall()

        # create list with all differences between original and modified databases
        # differences is a list of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
        i = 0
        differences = []
        for row in data_orig:
            differences.append((data_orig[i], data_copy[i]))
            i += 1
        con_orig.close()
        con_copy.close()
        metafunc.parametrize('orig, modif', differences)
    # generate data for test_ships_engine
    elif metafunc.function.__name__ == "test_ships_engine":
        """Checks if any engines property changed for each engine in table Engines"""
        # connection to original database
        # con_orig = sqlite3.connect(DATABASE_PATH_ORIG)
        # cur_orig = con_orig.cursor()

        data_orig = cur_orig.execute("SELECT * FROM Engines").fetchall()
        data_copy = cur_copy.execute("SELECT * FROM Engines").fetchall()

        # create list with all differences between original and modified databases
        # differences is a list of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
        i = 0
        differences = []
        for row in data_orig:
            differences.append((data_orig[i], data_copy[i]))
            i += 1
        con_orig.close()
        con_copy.close()
        metafunc.parametrize('orig, modif', differences)


def pytest_assertrepr_compare(op, left, right):
    """message for the failed test
    example:
    ship-200
            expected: engine-2 was engine-16
    """
    if isinstance(left, FailMsg) and isinstance(right, FailMsg) and op == "==":
        if left.val[0] != right.val[0]:
            original_part = left.val[0]
            different_part = right.val[0]
        elif left.val[1] != right.val[1]:
            original_part = left.val[1]
            different_part = right.val[1]
        elif left.val[2] != right.val[2]:
            original_part = left.val[2]
            different_part = right.val[2]
        elif left.val[3] != right.val[3]:
            original_part = left.val[3]
            different_part = right.val[3]
        elif left.val[4] != right.val[4]:
            original_part = left.val[4]
            different_part = right.val[4]
        elif left.val[5] != right.val[5]:
            original_part = left.val[5]
            different_part = right.val[5]
        # comma at the end of list is intentional
        return [
            f"{left.val[0]}",
            f"   expected: {original_part} was {different_part}",
        ]
