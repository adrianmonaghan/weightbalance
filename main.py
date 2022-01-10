from aircrafts.item import FuelTank
from aircrafts.item import Item
from aircrafts.r44 import R44

# The way you can get the place to get on the image. First find how many pixels is in one point or whatever, then,
# Set the bottom left corner to the origin, find the distance in inches and pounds from the origin in pixels and place
# a point there


def main():
    item = Item(1000, 2000, 3000, 4000, 5000, name = "Test item")
    for i in item:
        print(i)
    #print(tuple(item))
    print(item)
    fuel = FuelTank(1000,2000,3000,4000,5000,6000,7000, name = "Test fuel")
    print(fuel)
    heli = R44()
    heli.set_weight("FR_seat", 200)
    heli.set_weight("FR_bag",50)
    heli.set_vol("Main_fuel",20)
    heli.calculate_moments()
    print(heli.get_moments().values())
    heli.calculate_com()
    for x in heli.get_moments().values():
        print(x.get_name())
    print(heli)
    print("lat arm ", heli._lateral_arm)
    print("Lon arm ", heli._longitudinal_arm)
    print("Lon mom ", heli._longitudinal_moment)
    print("Lat mom ", heli._lateral_moment)
    print("Weight ", heli._weight)
    # print(item.get_vars())
    #print(fuel.get_vars())
    print(isinstance(fuel, FuelTank))
    print(isinstance(fuel, Item))
    print(isinstance(item, FuelTank))
    print(isinstance(item, Item))

if __name__ == "__main__":
    main()