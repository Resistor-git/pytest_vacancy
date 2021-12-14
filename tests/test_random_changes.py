import sqlite3

import pytest
from random import randint


def test_ships(orig, modif):
    assert orig == modif