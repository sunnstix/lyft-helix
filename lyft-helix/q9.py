# Really upset passengers

print("""Time of Day
people early in the morning might need to go to the airport or work
people late at night want to home fast and don't want to wait
if the time and location corresponds to a traffic event
Location""")


class Event:
    def __init__(self, driver_id: int, location: str, time: float) -> None:
        self.driver_id = driver_id
        self.location = location
        self.time = time

biased = list()

final_assesment = list()

def isBiased(allEvents : list):
    locations = dict()
    for event in allEvents:
        # if your ride is after 9 pm or before 9 am we assume you are most likely going
        # to work in the morning or coming home at night and will be impatient
        if event.time > 21.00 or event.time < 9.00:
            biased.append(True)
        else:
            biased.append(False)
        locations[event.location] = locations.get(event.location, 0) + 1
    average = sum(locations)/len(locations.keys())
    for i in len(allEvents):
        if biased(i) or locations[allEvents.location] > 1.5* average:
            final_assesment.append(True)
        else:
            final_assesment.append(False)
        


        
        
