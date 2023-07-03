
def connect_towers():
    num_towers = int(input("Enter the number of towers: "))
    num_buildings = int(input("Enter the number of buildings: "))

    towers = []
    buildings = []
    letters = ord('A')

    print("\nEnter the coordinates for the towers:")
    for i in range(num_towers):
        x, y = input(f"Tower {chr(letters)} coordinate: ").split()
        towers.append((x, y))
        letters += 1

    print("\nEnter the coordinates for the buildings:")
    for i in range(num_buildings):
        x, y = input(f"Building {chr(letters)} coordinate: ").split()
        buildings.append((x, y))
        letters += 1

    connections = []
    lst = towers + buildings

    for i in range(len(towers) - 1):
        lst.remove(towers[i])
        lst.remove(towers[i+1])
        if is_building_between(towers[i], towers[i+1], lst):
            print("no")
        else:
            connections.append((towers[i], towers[i+1]))
        lst.append(towers[i])
        lst.append(towers[i+1])

    print("\nTower connections:")
    for connection in connections:
        print(f"{connection[0]} -> {connection[1]}")


def is_building_between(tower1, tower2, buildings):
    x1 = int(tower1[0])
    y1 = int(tower1[1])
    x2 = int(tower2[0])
    y2 = int(tower2[1])

    for i in buildings:
        x3 = int(i[0])
        y3 = int(i[1])

        slope_AB = (y2 - y1) / (x2 - x1) if x2 - x1 != 0 else float('inf')
        slope_BC = (y3 - y2) / (x3 - x2) if x3 - x2 != 0 else float('inf')

        return slope_AB == slope_BC


print(is_building_between((1, 1), (5, 5), [(3, 3), (4, 3)]))
connect_towers()
