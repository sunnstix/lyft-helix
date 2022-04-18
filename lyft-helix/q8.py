# input is a list of lists of keywords from each review
# last string is the rating 

import numpy as np

def evaluateBias(reviews: list):
    scores = list()
    for review in reviews:
        scores.append(float(review[-1]))
    scoreNP = np.array(scores)
    oldAverage = np.average(scoreNP)
    scaled = np.abs(scoreNP - np.median(scoreNP))
    medianDeviation = np.median(scaled)
    s = scaled / medianDeviation
    biased = np.logical_and(s > 3, scoreNP < oldAverage)
    biasedWeights = np.where(biased, 1, 2)
    print(biasedWeights)
    newAverage = np.average(scoreNP,weights=biasedWeights)
    return (oldAverage, newAverage)

reviews = [['efficient', 'dirty', '3.5'], ['loud', 'messy', '.5'],['efficient', 'nice', '4.2']]
print(evaluateBias(reviews))