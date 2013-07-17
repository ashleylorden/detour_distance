import math

EARTH_RAD_IN_MI = 3960
EARTH_RAD_IN_KM = 6373

def calculate_distance(a, b):
    """
    accepts two points' lat and long and returns distance in miles
    calculated using spherical law of cosines, accurate for distances greater than 1m
    crow's flight distance, underestimates actual driving distance significantly
    """
    phi1 = math.radians(90.0 - a[0])
    phi2 = math.radians(90.0 - b[0])
    theta1 = math.radians(a[1])
    theta2 = math.radians(b[1])
    cos = (math.sin(phi1)*math.sin(phi2)*math.cos(theta1 - theta2) + 
        math.cos(phi1)*math.cos(phi2))
    arc = math.acos(cos)
    miles = arc*EARTH_RAD_IN_MI
    return miles

def shorter_detour_distance(a, b, c, d):
    """
    driver 1 starts a, ends b, 2 starts c, ends d. one detours to stop at all points.
    return total distance of the detour for the shorter route in miles.
    each point should be provided as a tuple of (latitude, longitude).
    note, to get extra distance as a result of the detour, would need to subtract original route.
    either driver must go a to c and b to d. Choose shorter of a-b (driver 2) and c-d (driver 1).
    """
    return calculate_distance(a, c) + min(calculate_distance(a, b), calculate_distance(c, d)) + \
    calculate_distance(d, b)

def main():
    home = (37.78533, -122.42497)
    lyft = (37.78990, -122.40078)
    pancho_villa = (37.76470, -122.42108)
    ikea = (37.83053, -122.29293)
    print "%.5f miles" % (shorter_detour_distance(home, lyft, pancho_villa, ikea))

if __name__ == "__main__":
    main()
