def derive(x):
  x = x[:-1]
  derivedCoeff = []
  p = len(x)
  for i in x:
    derivedCoeff.append(i * p)
    p = p - 1
  return derivedCoeff

def degree(a: list):
    return len(a) - 1

def trim(a: list):
    while a and a[0] == 0:
        a.pop(0)
    return a or [0]

def padd(a: list, b: list):
    a = a[:]
    b = b[:]
    while degree(a) < degree(b):
        a.insert(0, 0)
    while degree(b) < degree(a):
        b.insert(0, 0)
    return a, b

def polyAdd(a: list, b: list):
    ap, bp = padd(a, b)
    result = []
    for i in range(len(ap)):
        result.append(ap[i] + bp[i])
    return trim(result)

def polySubtract(a: list, b: list):
    ap, bp = padd(a, b)
    result = []
    for i in range(len(ap)):
        result.append(ap[i] - bp[i])
    return trim(result)

def polyMultScalar(a: list, scalar: float):
    result = []
    for i in a:
        result.append(i * scalar)
    return result

def polyRemainder(a: list, b: list):
    remainder = a[:]
    b = b[:]
    while degree(remainder) >= degree(b):
        leadingCoeff = remainder[0] / b[0]
        scaledTerm = polyMultScalar(b, leadingCoeff) + [0] * (degree(remainder) - degree(b))
        remainder = trim(polySubtract(remainder, scaledTerm))
    return trim(remainder)

def isZeroPoly(polynomial: list):
    return all(coef == 0 for coef in polynomial)

def polyBound(polynomial: list):
    polynomial = polynomial[:]
    fixedPolynomial = []
    for i in polynomial:
        fixedPolynomial.append(abs(i))
    M = 1 + max(fixedPolynomial[1:]) / fixedPolynomial[0]
    return [M * -1, M]
