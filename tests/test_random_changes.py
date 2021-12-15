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


def test_ships(orig, modif):
    """compares rows from original database (wargaming.db) with rows from modified temporary copy of database (db_copy_for_tst.db)
    compares data from table 'Ships' """
    original_ship = FailMsg(orig)
    modified_ship = FailMsg(modif)
    assert original_ship == modified_ship


def test_ships_weapon(orig, modif):
    """compares rows from original database (wargaming.db) with rows from modified temporary copy of database (db_copy_for_tst.db)
    compares data from table 'Weapons' """
    original_weapon = FailMsg(orig)
    modified_weapon = FailMsg(modif)
    assert original_weapon == modified_weapon


def test_ships_hull(orig, modif):
    """compares rows from original database (wargaming.db) with rows from modified temporary copy of database (db_copy_for_tst.db)
    compares data from table 'Hulls' """
    original_hull = FailMsg(orig)
    modified_hull = FailMsg(modif)
    assert original_hull == modified_hull


def test_ships_engine(orig, modif):
    """compares rows from original database (wargaming.db) with rows from modified temporary copy of database (db_copy_for_tst.db)
    compares data from table 'Engines' """
    original_engine = FailMsg(orig)
    modified_engine = FailMsg(modif)
    assert original_engine == modified_engine
