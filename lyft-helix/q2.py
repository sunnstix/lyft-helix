# question 2:
class Event:
    def __init__(self, driver_id: int, location: str, time: float) -> None:
        self.driver_id = driver_id
        self.location = location
        self.time = time
        
    def __str__(self) -> str:
        return ("{},{},{}".format(self.driver_id, self.location, self.time))
    
    def __eq__(self, o: object) -> bool:
        return (self.driver_id == o.driver_id and self.location == o.location and self.time == o.time)
    
class AllDrivers:
    def __init__(self) -> None:
        self.events = dict()
        pass
    
    def addEvent(self, event: Event) -> None:
        self.events[event.driver_id] = self.events.get(event.driver_id,list())
        self.events[event.driver_id].append(event)
    
    def delEvent(self, event: Event) -> None:
        if(event in self.events[event.driver_id]):
            self.events[event.driver_id].remove(event)
        else:
            return "Event was not found for driver with driver id " + str(event.driver_id) + "'s list"
        
    def getDriverInfo(self, driverId: int) -> Event:
        if (driverId in self.events):
            return self.events[driverId]
        else: 
            return "Driver with driver id " + str(driverId) + " does not have any events"
         

drivers = AllDrivers()
event1 = Event(1, "Michigan", 10)
event2 = Event(2, "Georgia", 12)
event3 = Event(2, "Alabama", 15.35)

print(str(event1))
drivers.addEvent(event1)
drivers.addEvent(event2)
drivers.addEvent(event3)
print(len(drivers.getDriverInfo(2)))
drivers.delEvent(Event(2, "Georgia", 12))
print(len(drivers.getDriverInfo(2)))

