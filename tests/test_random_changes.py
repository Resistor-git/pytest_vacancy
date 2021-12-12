import shutil
import pytest
import sqlite3

from pathlib import Path
from random import randint


# may be buggy; does it take the original copy or copy modified by test_change_ships_properties ???
def test_change_weapons_hulls_engines_properties(copy_db):
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
    
    # change Hulls table
    print("\nchanging properties in Weapons table")
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


    assert 1 == 1
