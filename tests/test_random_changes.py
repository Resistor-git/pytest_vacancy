import sqlite3

import pytest
from random import randint


def test_ships(what_changed_in_ships):
    assert what_changed_in_ships[0] == what_changed_in_ships[1]