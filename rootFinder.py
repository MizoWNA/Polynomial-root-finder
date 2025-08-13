from sturmsTheorem import *


def rootFind(poly: list):
    bounds = polyBound(poly)
    totalRoots = rootCount(poly, -bounds, bounds)

    boundsToRedo = []
    boundsCompleted = []

    boundsToRedo.append([-bounds, bounds])
    while len(boundsToRedo) > 0:
        [a, b] = boundsToRedo.pop()

        count = rootCount(poly, a, b)


        if count == 1:
            if (b - a) <= 1e-6:
                boundsCompleted.append([a, b])
            else:
                midpoint = (a+b) / 2
                boundsToRedo.append([a, midpoint])
                boundsToRedo.append([midpoint, b])


        elif count > 1 and (b - a) > 1e-6:
            midpoint = (a+b) / 2
            boundsToRedo.append([a, midpoint])
            boundsToRedo.append([midpoint, b])

    if len(boundsCompleted) == totalRoots:
        return boundsCompleted
    else: 
        return "ERROR! Ran into a problem!"
    

def newtonsMethod(poly: list, iterations: int):
    poly = poly[:]
    bounds = rootFind(poly)
    results = []
    if bounds == "ERROR! Ran into a problem!":
        return bounds
    else:
        for bound in bounds:
            x0 = (bound[0] + bound[1]) * 0.5
            for i in range(iterations):
                d = polyEval(derive(poly), x0)
                if d < 1e-12:
                    break
                else:
                    x1 = x0 - (polyEval(poly, x0) / d)
                    x0 = x1
            results.append(x0)

    return results


print(newtonsMethod([42, 0, 4, 0, -78, 1, -9, 25], 10))

