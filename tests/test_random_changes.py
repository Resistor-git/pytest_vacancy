import sqlite3

import pytest
from random import randint


# def test_what_changed_in_ships(copy_db, original_db):
#     """Checks if weapon or hull or engine was changed for each ship in table Ships"""
#     # connection to original database
#     con_orig = sqlite3.connect(original_db)
#     cur_orig = con_orig.cursor()

#     data_orig = cur_orig.execute("SELECT * FROM Ships").fetchall()
#     # print("original", data_orig)

#     # connection to temporary copy with changes
#     con_temp = sqlite3.connect(copy_db)
#     cur_temp = con_temp.cursor()

#     data_copy = cur_temp.execute("SELECT * FROM Ships").fetchall()
#     # print("copy:", data_copy)

#     # create list with all differences between original and modified databases
#     # differences is a list of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
#     i = 0
#     differences = []
#     for row in data_orig:
#         differences.append((data_orig[i], data_copy[i]))
#         i += 1
#     # print(differences)

#     for difference in differences:
#         # difference is tuple of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
#         print(difference)
#         # print('original', difference[0])
#         # print('copy', difference[1])
#         # compare each element of tuple to another element of tuple, in other words compare every property of ship from original db with every property of ship from temporary db
#         for n in range(0, len(differences[0][0])):
#             if difference[0][n] != difference[1][n]:
#                 # Ship-x, property-y (data from temp db)
#                 #   expected property-z (from original db), was property-y (from temp db)

#                 # difference[0] - original, difference[1] - temporary
#                 print(f"""{difference[1][0]}, {difference[1][n]}\n    expected {difference[0][n]}, was {difference[1][n]}""")

#                 # assert difference[0][n] == difference[1][n], f"{difference[1][0]}, {difference[1][n]}\n    expected {difference[0][n]}, was {difference[1][n]}"
#                 assert 1==1
    










# def orig_data(original_db):
#     """provides data from original database"""
#     # connection to original database
#     con_orig = sqlite3.connect(original_db)
#     cur_orig = con_orig.cursor()

#     data_orig = cur_orig.execute("SELECT * FROM Ships").fetchall()
    
#     return data_orig


# @pytest.mark.main_test
# def test_multiplication(test_input, expected_result):
#     assert test_input == expected_result

# @pytest.mark.main_test
# def test_multiplication(test_input, expected_result):
#     for test_tuple in test_list:
#         assert test_input == expected_result


# def what_changed_in_ships(copy_db, original_db):
#     """Checks if weapon or hull or engine was changed for each ship in table Ships"""
#     # connection to original database
#     con_orig = sqlite3.connect(original_db)
#     cur_orig = con_orig.cursor()

#     data_orig = cur_orig.execute("SELECT * FROM Ships").fetchall()
#     # print("original", data_orig)

#     # connection to temporary copy with changes
#     con_temp = sqlite3.connect(copy_db)
#     cur_temp = con_temp.cursor()

#     data_copy = cur_temp.execute("SELECT * FROM Ships").fetchall()
#     # print("copy:", data_copy)

#     # create list with all differences between original and modified databases
#     # differences is a list of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
#     i = 0
#     differences = []
#     for row in data_orig:
#         differences.append((data_orig[i], data_copy[i]))
#         i += 1
#     # print(differences)

#     for difference in differences:
#         # difference is tuple of tuples; each tuple looks like (('ship-200', 'weapon-20', 'hull-3', 'engine-6'), ('ship-200', 'weapon-20', 'hull-3', 'engine-7'))
#         print(difference)
#         # print('original', difference[0])
#         # print('copy', difference[1])
#         # compare each element of tuple to another element of tuple, in other words compare every property of ship from original db with every property of ship from temporary db
#         for n in range(0, len(differences[0][0])):
#             if difference[0][n] != difference[1][n]:
#                 # Ship-x, property-y (data from temp db)
#                 #   expected property-z (from original db), was property-y (from temp db)

#                 # difference[0] - original, difference[1] - temporary
#                 print(f"""{difference[1][0]}, {difference[1][n]}\n    expected {difference[0][n]}, was {difference[1][n]}""")
#                 yield difference


# @pytest.mark.parametrize("orig, modified", what_changed_in_ships('foo', 'foo'))
# def test_mt(orig, modified):
#     assert(orig == modified)

def test_ships(what_changed_in_ships):
    assert what_changed_in_ships[0] == what_changed_in_ships[1]