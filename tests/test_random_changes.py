import shutil
import pytest
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


def test_change_ships_properties(copy_db):
    """changes columns weapon, hull, engine in Ships table;
    takes the result of copy_db() and makes random changes in it
    'Для каждого корабля меняется на случайный один из компонентов: корпус, орудие или двигатель' - не уверен, что правильно понял. Я сделал так, что у всех кораблей
    меняется одинаковый компонент: корпус, орудие или двигатель.
    """
    # print("\nMYDEBUG", copy_db)
    # print("\nMYDEBUG", type(copy_db))
    con = sqlite3.connect(copy_db)
    cur = con.cursor()

    # change either weapon or hull or engine, based on random_number
    random_number = randint(1, 3)
    
    if random_number == 1:
        # change weapon
        print(f"\nrandom_number = {random_number}, changing weapon in Ships table")

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
        print(f"\nrandom_number = {random_number}, changing hull in Ships table")

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
        print(f"\nrandom_number = {random_number}, changing engine in Ships table")

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


# may be buggy; does it take the original copy or copy modified by test_change_ships_properties ???
def test_change_weapons_hulls_engines_properties(copy_db):
    """takes the result of copy_db() and makes random change in random property for each row of tables Weapons, Hulls, Engines"""
    con = sqlite3.connect(copy_db)
    cur = con.cursor()

    random_number = randint(1, 3)
    
    if random_number == 1:
        # change columns in Weapons table
        print(f"\nrandom_number = {random_number}, changing properties in Weapons table")
        # attmept to make code a little more flexible, without hardcoded number of rows
        # fetchall() returns a list of tuples, like [(15,)]
        quantity_of_rows_weapons = cur.execute("SELECT COUNT(*) FROM Weapons").fetchall()[0][0]

        for i in range(1, quantity_of_rows_weapons + 1):
            # "weapon" is used as a pointer in table, to show cur.execute which row should be changed
            weapon = "weapon-" + str(i)
            # max n = number of columns which can be changed (only one of them will be changed)
            n = randint(1, 3)
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
    
    elif random_number == 2:
        # change Hulls table
        print(f"\nrandom_number = {random_number}, changing properties in Weapons table")
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
    
    elif random_number == 3:
        # change Engines table
        print(f"\nrandom_number = {random_number}, changing properties in Engines table")
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



    assert 1 == 1
