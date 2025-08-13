from polyTools import *

def sumCounter(polynomial: list, x: float):
    sequences = sequenceBuilder(polynomial)  # build the Sturm sequence
    values = []
    for poly in sequences:
        val = 0
        deg = len(poly) - 1
        for coeff in poly:
            val += coeff * (x ** deg)
            deg -= 1
        values.append(val)
    return values

def sequenceBuilder(polynomial: list):
    polynomial = polynomial[:]
    series = []
    series.append(polynomial)
    series.append(derive(polynomial))
    
    while True:
        nextTerm = polyMultScalar(polyRemainder(series[-2], series[-1]), -1)
        if isZeroPoly(nextTerm):
            break
        if degree(nextTerm) == 0:
            series.append(nextTerm)
            break
        series.append(nextTerm)
    return series

def signing(sums: list):
    signs = ""
    for val in sums:
        if val > 1e-12:
            signs += "+"
        elif val < -1e-12:
            signs += "-"
        else:
            signs += "0"
    signs = signs.replace("0", "")
    count = signs.count("+-") + signs.count("-+")
    return count

def rootCount(poly: list, a: float, b: float):
    lowerBound = signing(sumCounter(poly, a))
    upperBound = signing(sumCounter(poly, b))
    return lowerBound - upperBound

