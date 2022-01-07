from aircrafts.item import FuelTank
from aircrafts.item import Item
from aircrafts.r44 import R44


def main():
    item = Item(1000, 2000, 3000, 4000, 5000)
    for i in item:
        print(i)
    print(tuple(item))
    print(item)
    fuel = FuelTank(1000,2000,3000,4000,5000,6000,7000)
    print(fuel)
    heli = R44()
    heli.set_weight("FR_seat", 200)
    heli.set_weight("FR_bag",50)
    heli.set_vol("Main_fuel",20)
    heli.calculate_moments()
    print(heli)
    heli.calculate_com()
    print("lat arm ", heli._lateral_arm)
    print("Lon arm ", heli._longitudinal_arm)
    print("Lon mom ", heli._longitudinal_moment)
    print("Lat mom ", heli._lateral_moment)
    print("Weight ", heli._weight)

if __name__ == "__main__":
    main()