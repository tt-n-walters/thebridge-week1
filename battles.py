import random

knights = []
for i in range(10):
    knight = {
        "type": "knight",
        "health": random.randint(35, 45),
        "attack": round(random.uniform(5, 7), 1),
        "defence": 9,
        "speed": 1,
        "luck": 2.5
    }
    knights.append(knight)


scouts = []
for i in range(20):
    scout = {
        "type": "scout",
        "health": random.randint(23, 27),
        "attack": round(random.uniform(2, 4), 1),
        "defence": 1,
        "speed": 8,
        "luck": 15
    }
    scouts.append(scout)





def attack(unit_a, unit_b):

    speed_difference = max(unit_a["speed"] - unit_b["speed"], 1)
    for i in range(speed_difference):
        damage = unit_a["attack"] / unit_b["defence"]
        if random.randint(0, 100) < unit_a["luck"]:
            damage = damage * 2
            # print(unit_a["type"], "Critical hit!", damage)
        unit_b["health"] = round(unit_b["health"] - damage, 2)
        # Set the unit health to 0 at minimum.
        unit_b["health"] = max(unit_b["health"], 0.0)



def fight(unit_a, unit_b):
    # Simulate fight between 2 units
    # Attack one another until 1 has 0 health left
    print("\x1b[0;0H\x1b[0JFIGHT")
    print("Type:", unit_a["type"], "Health:", unit_a["health"])
    print("Type:", unit_b["type"], "Health:", unit_b["health"])
    print()

    while unit_a["health"] > 0 and unit_b["health"] > 0:
        attack(unit_a, unit_b)          # unit_a attack unit_b
        if unit_b["health"] > 0:        # if unit_b is still alive, attack unit_a
            attack(unit_b, unit_a)
    
    print()
    print("Type:", unit_a["type"], "Health:", unit_a["health"])
    print("Type:", unit_b["type"], "Health:", unit_b["health"])
    print()


def battle(army_a, army_b):
    unit_a = None            # Create the unit variables, so that
    unit_b = None            # the loop can run before we have selected units.
    while True:
        # Take the first unit of each army
        if not unit_a:
            unit_a = army_a.pop(0)
        if not unit_b:
            unit_b = army_b.pop(0)
        
        # Make them fight to the death
        fight(unit_a, unit_b)

        # Remove the unit that died
        if unit_a["health"] <= 0:
            unit_a = None
        elif unit_b["health"] <= 0:
            unit_b = None
        
        # When one army runs out of units, stop the loop
        if len(army_a) == 0 or len(army_b) == 0:
            break
    
    print("Army A:", len(army_a))
    print("Army B:", len(army_b))


def create_unit(unit_name):
    file = open("units/" + unit_name + ".txt", "r")
    data = file.read()
    file.close()

    data = data.splitlines()

    #     PARSING    #

    # Empty dictionary for the unit
    unit = {}
    for line in data:
        item = line.split()
        key, value = item

        if key == "type":
            unit[key] = value
            continue
        
        if "," in value:
            # We have a range of numbers eg.  "23,27"
            minimum, maximum = value.split(",")
            if key == "health":
                value = random.randint(int(minimum), int(maximum))
            else:
                value = round(random.uniform(int(minimum), int(maximum)), 1)
            # Add the random value to the dictionary
            unit[key] = value
            continue
        
        # Check for an integer or a float
        if value.isdigit():
            value = int(value)
        else:
            value = float(value)
        unit[key] = value
    return unit


def create_army(unit_names, army_name):
    army = []
    for unit in unit_names:
        print("\x1b[0;0H\x1b[0JCreating", unit)
        unit = create_unit(unit)
        army.append(unit)
    return army


units = ["knight"] * 10000 + ["scout"] * 12345 + ["archer"] * 9999
army_a = create_army(units, "Army 1")

units = ["knight"] * 4000 + ["scout"] * 100000 + ["archer"] * 25000
army_b = create_army(units, "Army B")

battle(army_a, army_b)