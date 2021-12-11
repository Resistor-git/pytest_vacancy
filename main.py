import sqlite3
from random import randint
from my_classes import Ship, Weapon, Hull, Engine

con = sqlite3.connect('wargaming.db')
# con = sqlite3.connect(":memory:")
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
        print("table already exists")
    

def insert_ships():
    """randomly insert values in table Ships"""
    # class instance: Ship(ship, hull, engine, weapon)
    # number_of_ships = list(range(1, 201))
    # for num in number_of_ships:
    #     rand_num_hull = randint(1, 5)
    #     rand_num_engine = randint(1, 6)
    #     rand_num_weapon = randint(1, 20)

    #     ship_instance = Ship(f"ship-{num}", f"hull-{rand_num_hull}", f"engine-{rand_num_engine}", f"weapon-{rand_num_weapon}")
    #     print(ship_instance)
    #     with con:
    #         cur.execute("INSERT INTO Ships (ship, hull, engine, weapon) VALUES (:ship, :hull, :engine, :weapon)",
    #                     {"ship" : ship_instance.ship, "hull" : ship_instance.hull, "engine" : ship_instance.engine, "weapon" : ship_instance.weapon,})

    list_of_ships = []
    for num in list(range(1, 201)):
        rand_num_hull = randint(1, 5)
        rand_num_engine = randint(1, 6)
        rand_num_weapon = randint(1, 20)
        ship_instance = Ship(f"ship-{num}", f"hull-{rand_num_hull}", f"engine-{rand_num_engine}", f"weapon-{rand_num_weapon}")

        the_ship_params = (ship_instance.ship, ship_instance.hull, ship_instance.engine, ship_instance.weapon)
        print(the_ship_params)
        list_of_ships.append(the_ship_params)
        #print(list_of_ships)

    with con:
        cur.executemany("INSERT INTO Ships (ship, hull, engine, weapon) VALUES (?, ?, ?, ?)", list_of_ships)


def insert_weapons():
    """randomly insert values in table Weapons"""
    # class instance: Weapon(weapon, reload_speed, rotation_speed, diameter, power_volley, count)
    number_of_weapons = list(range(1, 21))
    for num in number_of_weapons:
        weapon_instance = Weapon(f"weapon-{num}", randint(1, 20), randint(1, 20), randint(1, 20),
                                randint(1, 20), randint(1, 20))
        print(weapon_instance)
        with con:
            cur.execute("""INSERT INTO Weapons (weapon, reload_speed, rotation_speed, diameter, power_volley, count)
                        VALUES (:weapon, :reload_speed, :rotation_speed, :diameter, :power_volley, :count)""",
                        {"weapon" : weapon_instance.weapon, "reload_speed" : weapon_instance.reload_speed, "rotation_speed" : weapon_instance.rotation_speed,
                        "diameter" : weapon_instance.diameter, "power_volley" : weapon_instance.power_volley, "count" : weapon_instance.count})


def insert_hulls():
    """randomly insert values in table Hulls"""
    # class instance: Hull(hull, armor, type, capacity)
    number_of_hulls = list(range(1, 6))
    for num in number_of_hulls:
        hull_instance = Hull(f"hull-{num}", randint(1, 20), randint(1, 20), randint(1, 20))
        print(hull_instance)
        with con:
            cur.execute("""INSERT INTO Hulls (hull, armor, type, capacity) 
                        VALUES (:hull, :armor, :type, :capacity)""",
                        {"hull" : hull_instance.hull, "armor" : hull_instance.armor, "type" : hull_instance.type, "capacity" : hull_instance.capacity})


def insert_engines():
    """randomly insert values in table Engines"""
    # class instance: Engine(engine, power, type)
    number_of_engines = list(range(1, 7))
    for num in number_of_engines:
        engine_instance = Engine(f"engine-{num}", randint(1, 20), randint(1, 20))
        print(engine_instance)
        with con:
            cur.execute("INSERT INTO Engines (engine, power, type) VALUES (:engine, :power, :type)",
                        {"engine" : engine_instance.engine, "power" : engine_instance.power, "type" : engine_instance.type})


create_db()
insert_ships()
insert_weapons()
insert_hulls()
insert_engines()

con.close()

# https://www.youtube.com/watch?v=aJVvffGlwQU&list=PLJsmaNFr5mNqSeuNepT3IaMrgzRMm9lQR&index=1
# https://code.visualstudio.com/docs/python/testing