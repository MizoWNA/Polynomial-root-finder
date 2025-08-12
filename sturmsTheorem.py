from polyTools import *

def sequenceBuilder(polynomial: list):
    polynomial = polynomial[:]
    series = []
    lastTerm = polynomial
    series.append(polynomial)
    series.append(derive(polynomial))
    while True:
        nextTerm = polyMultScalar(polyRemainder(series[-2], series[-1]), -1)
        if isZeroPoly(nextTerm):
            break
        series.append(nextTerm)
    return series

def sumCounter(polynomial: list, inp: int):
    sequences = sequenceBuilder(polynomial)
    totalsums = []
    for polynomial in sequences:
        deg = degree(polynomial)
        sum = 0
        for term in polynomial:
            sum += term * pow(inp, deg)
            deg -= 1
        totalsums.append(sum)
    return totalsums

polyinp = [1, 1, -1, -1]
print(sumCounter(polyinp, polyBound(polyinp)[1]))

