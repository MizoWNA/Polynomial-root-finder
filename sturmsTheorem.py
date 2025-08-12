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

def signing(sums: list):
    signs = ""
    for i in sums:
        if i > 1e-12:
            signs += "+"
        if i < -1e-12:
            signs += "-"
        if abs(i) <= 1e-12:
            signs += "0"
    signs = signs.replace("0", "")
    sumSigns = 0
    sumSigns += signs.count("+-")
    sumSigns += signs.count("-+")
    return sumSigns

def rootCount(poly: list):
    M = polyBound(poly)
    lowerBound = signing(sumCounter(poly, -M))
    upperBound = signing(sumCounter(poly, M))
    return lowerBound - upperBound

polyinp = [1, 1, -1, -1]
print(rootCount(polyinp))

