import time

class Person:
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y

class Driver(Person):
    def __init__(self, driver_id:int, x: int, y:int) -> None:
        self.driver_id = driver_id
        Person.__init__(x,y)
        
class Passenger(Person):
    def __init__(self, name:str, x:int, y:int) -> None:
        self.name = name
        Person.__init__(x,y)

class MatchMaker:
    def __init__(self) -> None:
        self.drivers = list()
        
    def addDriver(self, driver: Driver) -> None:
        self.drivers.append(driver)
        
    # We will return the best available driver for the person who has been waiting
    # in the passenger queue the longest. We wil return by the shortest euclidian distance
    # given the x and y coordinates of both the driver and the passenger
    # this will allow for passengers to get served sequentially, while also allowing
    # for minimizatiion in driver distance to reach the next passenger
    # as the secondary goal in the case that we have more than 1 driver available at a time
    def match(self, passenger: Passenger) -> Driver:
        while len(self.drivers) == 0:
            time.sleep(5)
        distanceSort = lambda driver1, driver2: ((driver1.x - passenger.x)**2 + (driver1.y - passenger.y)**2) < ((driver2.x - passenger.x)**2 + (driver2.y - passenger.y)**2)
        selectedDriver = sorted(self.drivers,key = distanceSort)[0]
        self.drivers.remove(selectedDriver)
        return selectedDriver


print("""We will return the best available driver for the person who has been waiting
    in the passenger queue the longest. We wil return by the shortest euclidian distance
    given the x and y coordinates of both the driver and the passenger
    this will allow for passengers to get served sequentially, while also allowing
    for minimizatiion in driver distance to reach the next passenger
    as the secondary goal in the case that we have more than 1 driver available at a time""")