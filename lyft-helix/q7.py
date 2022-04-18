# input is a list of lists of keywords from each review
# last string is the rating 

import numpy as np

def evaluateBias(reviews: list):
    scores = list()
    for review in reviews:
        scores.append(float(review[-1]))
    scoreNP = np.array(scores)
    scaled = np.abs(scoreNP - np.median(scoreNP))
    medianDeviation = np.median(scaled)
    s = scaled / medianDeviation
    biased = list(s > 3)
    out = list()
    for (bias, review, score) in zip(biased, reviews, scores):
        out.append(str(review) + ("- bias" if bias and score < np.average(scoreNP) else "- no bias"))
    return out

reviews = [['efficient', 'dirty', '3.5'], ['loud', 'messy', '.5'],['efficient', 'nice', '4.2']]
print(evaluateBias(reviews))