# FIND DESTINATION AIRPORT 
# FIND ORIGIN AIRPORT

def filter_takeoff_land(routes,takeoff, land):
    for route in routes:
        takeoff.append(route[0])
        land.append(route[1])

def find_origin(routes, takeoff, land):
    return ([t for t in takeoff if t not in land])

def find_destin(routes, takeoff,land):
    return ([t for t in land if t not in takeoff])

def find_route(routes, target):
    res = []
    land = []
    fs = []
    for route in routes:
        if route[0] == target:
            res.append((route[0], route[1]))
        elif route[1] == target:
            land.append((route[0], route[1]))
    for route in routes:
        if route[1] not in res:
            fs.append(route)
        else:
            while route[1] in routes:
                fs.append(route)
    print(fs)

def main():
    routes = [ ["GRU","POR"],["ITA","FRA"], ["POR","ITA"], ["FRA", "VIX"], ["FRA","ITA" ]]
    takeoff = []
    land = []
    filter_takeoff_land(routes,takeoff, land)
    
    airp = input('Type airport: ')
    
    find_route(routes,airp)
    
if __name__ == "__main__":
    main()