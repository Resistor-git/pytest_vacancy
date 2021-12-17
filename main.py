import sqlite3
from random import randint
from my_classes import Ship, Weapon, Hull, Engine

con = sqlite3.connect('wargaming.db')
cur = con.cursor()


def create_db():
    """create database with 4 tables: Ships, Weapons, Hulls, Engines
    if database already exists - do nothing and print message"""
    try:
        with con:
            cur.execute("""CREATE TABLE Ships (
                        ship TEXT PRIMARY KEY,
                        weapon TEXT,
                        hull TEXT,
                        engine TEXT,
                        FOREIGN KEY (weapon) REFERENCES Weapons(weapon),
                        FOREIGN KEY (hull) REFERENCES Hulls(hull),
                        FOREIGN KEY (engine) REFERENCES Engines(engine)
                        )""")
        with con:
            cur.execute("""CREATE TABLE Weapons (
                        weapon TEXT PRIMARY KEY,
                        reload_speed INT,
                        rotation_speed TEXT,
                        diameter INT,
                        power_volley INT,
                        count INT
                        )""")
        with con:
            cur.execute("""CREATE TABLE Hulls (
                        hull TEXT PRIMARY KEY,
                        armor INT,
                        type INT,
                        capacity INT
                        )""")
        with con:
            cur.execute("""CREATE TABLE Engines(
                        engine TEXT PRIMARY KEY,
                        power INT,
                        type INT
                        )""")
    except sqlite3.OperationalError:
        print("database or table already exists")
        exit()
    

def insert_ships():
    """randomly insert values in table Ships"""
    # list_of_ships used in cur.executemany; contains tuples, each tuple represents a ship
    list_of_ships = []

    for num in list(range(1, 201)):
        rand_num_hull = randint(1, 5)
        rand_num_engine = randint(1, 6)
        rand_num_weapon = randint(1, 20)
        # class instance: Ship(ship, hull, engine, weapon)
        ship_instance = Ship(f"ship-{num}", f"hull-{rand_num_hull}", f"engine-{rand_num_engine}", f"weapon-{rand_num_weapon}")
        # print(ship_instance)

        # the_ship_params is a tuple, contains data about one ship
        the_ship_params = (ship_instance.ship, ship_instance.hull, ship_instance.engine, ship_instance.weapon)
        list_of_ships.append(the_ship_params)

    with con:
        cur.executemany("INSERT INTO Ships (ship, hull, engine, weapon) VALUES (?, ?, ?, ?)", list_of_ships)



def insert_weapons():
    """randomly insert values in table Weapons"""
    # list_of_weapons used in cur.executemany; contains tuples, each tuple represents a weapon
    list_of_weapons = []
    number_of_weapons = list(range(1, 21))

    for num in number_of_weapons:
        # class instance: Weapon(weapon, reload_speed, rotation_speed, diameter, power_volley, count)
        weapon_instance = Weapon(f"weapon-{num}", randint(1, 20), randint(1, 20), randint(1, 20),
                                randint(1, 20), randint(1, 20))
        # print(weapon_instance)

        the_weapon_params = (weapon_instance.weapon, weapon_instance.reload_speed, weapon_instance.rotation_speed, weapon_instance.diameter, weapon_instance.power_volley, weapon_instance.count)
        list_of_weapons.append(the_weapon_params)

    with con:
        cur.executemany("""INSERT INTO Weapons (weapon, reload_speed, rotation_speed, diameter, power_volley, count)
                        VALUES (?, ?, ?, ?, ?, ?)""", list_of_weapons)


def insert_hulls():
    """randomly insert values in table Hulls"""
    # list_of_hulls used in cur.executemany; contains tuples, each tuple represents a hull
    list_of_hulls = []
    number_of_hulls = list(range(1, 6))

    for num in number_of_hulls:
        # class instance: Hull(hull, armor, type, capacity)
        hull_instance = Hull(f"hull-{num}", randint(1, 20), randint(1, 20), randint(1, 20))
        # print(hull_instance)

        the_hull_params = (hull_instance.hull, hull_instance.armor, hull_instance.type, hull_instance.capacity)
        list_of_hulls.append(the_hull_params)

    with con:
        cur.executemany("""INSERT INTO Hulls (hull, armor, type, capacity) 
                        VALUES (?, ?, ?, ?)""", list_of_hulls)


def insert_engines():
    """randomly insert values in table Engines"""
    # list_of_engines used in cur.executemany; contains tuples, each tuple represents an engine
    list_of_engines = []
    number_of_engines = list(range(1, 7))

    for num in number_of_engines:
        # class instance: Engine(engine, power, type)
        engine_instance = Engine(f"engine-{num}", randint(1, 20), randint(1, 20))
        # print(engine_instance)

        the_engine_params = (engine_instance.engine, engine_instance.power, engine_instance.type)
        # print(the_engine_params)
        list_of_engines.append(the_engine_params)

    with con:
        cur.executemany("INSERT INTO Engines (engine, power, type) VALUES (?, ?, ?)", list_of_engines)


create_db()
insert_ships()
insert_weapons()
insert_hulls()
insert_engines()

con.close()
