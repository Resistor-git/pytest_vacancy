class Ship:
    def __init__(self, ship, hull, engine, weapon):
        self.ship = ship
        self.hull = hull
        self.engine = engine
        self.weapon = weapon
    
    def __repr__(self):
        return f"Ship: {self.ship}, Hull: {self.hull}, Engine: {self.engine}, Weapon: {self.weapon}"


class Weapon:
    def __init__(self, weapon, reload_speed, rotation_speed, diameter, power_volley, count):
        self.weapon = weapon
        self.reload_speed = reload_speed
        self.rotation_speed = rotation_speed
        self.diameter = diameter
        self.power_volley = power_volley
        self.count = count
    
    def __repr__(self):
        return f"Weapon: {self.weapon}, Reload speed: {self.reload_speed}, Rotation speed: {self.rotation_speed}, Diameter: {self.diameter}, Power volley: {self.power_volley}, Count: {self.count}"


class Hull:
    def __init__(self, hull, armor, type, capacity):
        self.hull = hull
        self.armor = armor
        self.type = type
        self.capacity = capacity
    
    def __repr__(self):
        return f"Hull: {self.hull}, Armor: {self.armor}, Type: {self.type}, Capacity: {self.capacity}"


class Engine:
    def __init__(self, engine, power, type):
        self.engine = engine
        self.power = power
        self.type = type
            
    def __repr__(self):
        return f"Engine: {self.engine}, Power: {self.power}, Type: {self.type}"