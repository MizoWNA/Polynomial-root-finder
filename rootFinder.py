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

print(rootFind([42, 0, 4, 0, -78, 1, -9, 25]))