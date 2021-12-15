import sqlite3

import pytest
from random import randint


# def test_ships(orig, modif):
#     assert orig == modif


# this class is here because I'm lazy (it should be in my_classes.py)
class FailMsg:
    def __init__(self, val):
        self.val = val

    def __eq__(self, other):
        return self.val == other.val


# compares rows from original database (wargaming.db) with rows from modified temporary copy of database (db_copy_for_tst.db)
def test_ships(orig, modif):
    row1 = FailMsg(orig)
    row2 = FailMsg(modif)
    assert row1 == row2
