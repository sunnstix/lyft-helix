# input price and milage for every 30 minutes and determine peak price times
# we assume that input starts at midnight and ends at 11:30 pm and we will output an
# array of true or false values for each half hour with true meaning there is peak pricing
# and false for normal pricing

# we assume input is a list with n elements and each elements denoting the half hour segment of the day in chronological order with element value as a tuple of price and distance
import heapq

# Produces generator for peak times
def calcPeakPrices(priceTimes : list):
    costs = list()
    for time, (price, distance) in enumerate(priceTimes):
        heapq.heappush(costs, (-price/distance, time))
        
        # we say that peak pricing is the top 25% of pricing throughout the day
    for _ in range(int(0.25*len(priceTimes))):
        cost, peak_time = heapq.heappop(costs)
        yield (peak_time, -cost)
        

input_list = [(5,1),(4,2),(10,5),(10,2),(12,3)]

for output in calcPeakPrices(input_list):
    print(output)