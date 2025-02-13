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

def main():
    routes = [ ["GRU","POR"],["ITA","FRA"], ["POR","ITA"], ["FRA", "VIX"] ]
    takeoff = []
    land = []
    filter_takeoff_land(routes,takeoff, land)
    
    print(find_origin(routes,takeoff,land))
    
if __name__ == "__main__":
    main()