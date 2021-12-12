import shutil
import pytest
import sqlite3

from pathlib import Path
from random import randint


def test_what_changed_in_ships(copy_db, original_db):
    """Checks if weapon or hull or engine was changed for each ship in table Ships"""
    # connection to original table
    # con_orig = ???

    # connection to temporary copy with changes
    con_temp = sqlite3.connect(copy_db)
    cur_temp = con_temp.cursor()

    foo = cur_temp.execute("SELECT * FROM Ships WHERE ship = :ship", {"ship" : 'ship-1'}).fetchall()
    print("copy:", foo)

    # connection to original database
    con_orig = sqlite3.connect(original_db)
    cur_orig = con_temp.cursor()

    bar = cur_temp.execute("SELECT * FROM Ships WHERE ship = :ship", {"ship" : 'ship-1'}).fetchall()
    print("original", foo)

    assert 11==11