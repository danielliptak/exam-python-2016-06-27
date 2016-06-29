
# Create a Rocket class
# It should take 3 parameters in its constructor
# 1st parameter: the type of the rocket as a string, "falcon1" or "falcon9"
# 2nd parameter: the starting fuel level as a number
# 3rd parameter: number of launches as a number
#
# It should have 3 methods:
#
# launch()
# it should use 1 fuel if it's a falcon1 and 9 if it's a falcon9
# it should increment the launches by one

# refill()
# it should refill the rocket's fuel level to 5 if falcon1 and to 20 if falcon9
# it should return the used fuel
# example: if the rocket is a falcon1 and has fuel level 3, then it should return 2
# #
# getStats()
# it should return its stats as a string like: "name: falcon9, fuel: 11"

# Create a SpaceX class
# it should take 1 parameter in its constructor
# 1st parameter: the stored fuel
#
# it should have 4 methods:
#
# addRocket(rocket)
# it should add a new rocket to SpaceX that is given in its first parameter
# #
# refill_all()
# it should refill all of its rockets with fuel and substract the needed fuel from the storage

# launch_all()
# it should launch all the rockets
#
# buy_fuel(amount)
# it should increase stored fuel by amount
# #
# getStats()
# it should return its stats as a sting like: "rockets: 3, fuel: 100, launches: 1"
#

# The following code should work with the classes

class Rocket(object):
    def __init__(self, rocket_type, fuel_lev, launch_num):
        self.rocket_type = rocket_type
        self.fuel_lev = fuel_lev
        self.launch_num = launch_num
    def launch(self):
        if self.rocket_type == 'falcon1':
            self.fuel_lev -= 1
            self.launch_num += 1
        elif self.rocket_type == 'falcon9':
            self.fuel_lev -= 1
            self.launch_num += 1
    def refill(self):
        if self.rocket_type == 'falcon1':
            used_fuel = 5 - self.fuel_lev
            self.fuel_lev = 5
            return used_fuel
        elif self.rocket_type == 'falcon9':
            used_fuel = 20 - self.fuel_lev
            self.fuel_lev = 20
            return used_fuel
    def getStats(self):
        return 'Name: {}, Fuel: '.format(self.rocket_type, self.fuel_lev)

class SpaceX(object):
    def __init__(self, stored_fuel):
        self.stored_fuel = stored_fuel
        self.stored_rockets = []
    def addRocket(self, rocket):
        self.stored_rockets.append(rocket)
    def refill_all(self):
        for obj in range(len(self.stored_rockets)):
            self.stored_fuel = self.stored_fuel - self.stored_rockets[obj].refill()
    def launch_all(self):
        for obj in range(len(self.stored_rockets)):
            self.stored_rockets[obj].launch()
    def buy_fuel(self, amount):
        self.stored_fuel += amount
    def sum_launches(self):
        total_launches = 0
        for obj in range(len(self.stored_rockets)):
            total_launches += self.stored_rockets[obj].launch_num
        return total_launches
    def getStats(self):
        return 'Rocket: {}, Fuel: {}, launches: {}'.format(len(self.stored_rockets), self.stored_fuel, self.sum_launches())


space_x = SpaceX(100)
falcon1 = Rocket('falcon1', 0, 0)
falcon9 = Rocket('falcon9', 0, 0)
returned_falcon9 = Rocket('falcon9', 11, 1)

print(returned_falcon9.getStats()) # name: falcon9, fuel: 11

space_x.addRocket(falcon1)
space_x.addRocket(falcon9)
space_x.addRocket(returned_falcon9)

print(space_x.getStats()) # rockets: 3, fuel: 100, launches: 1
space_x.refill_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 1
space_x.launch_all()
print(space_x.getStats()) # rockets: 3, fuel: 66, launches: 4
space_x.buy_fuel(50)
print(space_x.getStats()) # rockets: 3, fuel: 116, launches: 4
