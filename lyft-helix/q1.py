# Question 1:
# What data structure would you use and why?

# With regards to access patterns, I think that, without additional context on how this data will be used,
# it would reasonable to say that an application would more likely request times of accidents at a particular location.
# The tendency to translate a location into a series of timestamps at that location results in my belief that core 
# data structure should be some form of hashmap (dict in Python) that is indexed on location as a key and stores
# a mutable list of times as it's value

class Accidents:
    def __init__(self) -> None:
        self.accidents = dict()
    
    # Adds accident to list of accidents
    def new_accident(self, location, time) -> None:
        self.accidents[location] = self.accidents.get(location,list()).append(time)
    
    # Return list of accidents at location
    def get_accidents(self, location) -> list:
        return self.accidents[location]



