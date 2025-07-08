from polyTools import *

def sequenceBuilder(polynomial: list):
    polynomial = polynomial[:]
    series = []
    lastTerm = polynomial
    series.append(polynomial)
    series.append(derive(polynomial))
    while len(lastTerm) != 1:
        lastTerm = polyMultScalar(polyRemainder(series[-2], series[-1]), -1)
        series.append(lastTerm)
    return series