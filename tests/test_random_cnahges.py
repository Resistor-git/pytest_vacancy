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


def test_bar(copy_db):
    """takes the result of copy_db() and makes random changes in it"""
    print("\nMYDEBUG", copy_db)
    print("\nMYDEBUG", type(copy_db))
    con = sqlite3.connect(copy_db)
    cur = con.cursor()
    with con:
        # randomize weapon for each ship (each row in table Ships)
        rand_weapon = randint(1, 20)
        cur.execute("UPDATE Ships SET weapon = :rand_weapon WHERE ship", {"rand_weapon" : rand_weapon})
    assert 1 == 1

