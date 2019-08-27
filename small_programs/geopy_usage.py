import geopy.distance

coordinate1 = (39.289374, -94.573468)
coordinate2 = (39.289377, -94.574242)

displacement = geopy.distance.distance(coordinate1, coordinate2).feet
print(f"The displacement between the two coordinates is {displacement}")