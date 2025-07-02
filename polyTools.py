def derive(x):
  x = x[:-1]
  derivedCoeff = []
  p = len(x)
  for i in x:
    derivedCoeff.append(i * p)
    p = p - 1
  return derivedCoeff



def degree(poly):
    return len(poly) - 1

def trim(poly):
    while poly and poly[0] == 0:
        poly.pop(0)
    return poly or [0]

def padd(a: list, b: list):
    # Darlin, here we create a copy of the original inputs so we dont run into problems if we reuse the inputs somewhere else
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




