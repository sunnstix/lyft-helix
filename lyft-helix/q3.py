# list of sets with driver ids, times, and locations
# 1st list has location and time for each element
# 2nd list has driver ID with location and times they were in that location
# return driver Ids with times and locations they would have been affected by  given with times and list of sets with driver IDs
# impact means you were within the spot 30 minutes +- time or .30

# input is a list of these
import math 

class Event:
    def __init__(self, driver_id: int, location: str, time: float) -> None:
        self.driver_id = driver_id
        self.location = location
        self.time = time
        
    def __str__(self) -> str:
        return ("{},{},{}".format(self.driver_id, self.location, self.time))
    
    def __eq__(self, o: object) -> bool:
        return (self.driver_id == o.driver_id and self.location == o.location and self.time == o.time)

class Hotspot:
    def __init__(self, location, time) -> None:
        self.location = location
        self.time = time
        
class AllDrivers:
    def __init__(self) -> None:
        self.events = dict()
        self.drivers = set()
    
    def addEvent(self, event: Event) -> None:
        updatedInfo = self.events.get(event.location,list())
        updatedInfo.append(event)
        self.events[event.location] = updatedInfo
        
        # add driver if new
        self.drivers.add(event.driver_id)
    
    def delEvent(self, event: Event) -> None:
        if(event in self.events[event.location]):
            self.events[event.location].remove(event)
        else:
            return "Event was not found for driver with driver id " + str(event.driver_id) + "'s list"
        
    def getDriverInfo(self, driverId: int) -> Event:
        if (driverId in self.events):
            return self.events[driverId]
        else: 
            return "Driver with driver id " + str(driverId) + " does not have any events"
        
        # list of hotspots will have locations and corresponding times
    def getImpactedDrivers(self, hotspots: list):
        impactedDriver = dict()
        for driver_id in self.drivers:
            impactedDriver[driver_id] = list()
            
        for hotspot in hotspots:
            for event in self.events[hotspot.location]:
                if math.abs(hotspot.time - event.time) < 0.3:
                    impactedDriver[event.driver_id].append((event.location,event.time))
        
        for driver_id, impactedList in impactedDriver.items():
            print(driver_id, impactedList)
                
        