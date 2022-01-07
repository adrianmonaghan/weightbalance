from aircrafts.item import Item
from aircrafts.item import FuelTank


class R44:

    class ItemNotInAircraftError(Exception):
        pass

    def __init__(self):
        self._moments = {
            "empty": Item(1466.2, 105.91, 155285.242, 0.31, 454.522),
            "FR_seat": Item(0, 49.5, 0, 12.2, 0),
            "FL_seat": Item(0, 49.5, 0, -10.4, 0),
            "BR_seat_bag": Item(0, 79.5, 0, 12.2, 0),
            "BL_seat_bag": Item(0, 79.5, 0, -12.2, 0),
            "FR_bag": Item(0, 44, 0, 11.5, 0),
            "FL_bag": Item(0, 44, 0, -11.5, 0),
            "FR_door": Item(7.5, 49.4, 370.5, 24, 180),
            "FL_door": Item(7.5, 49.4, 370.5, -24, -180),
            "BR_door": Item(7, 75.4, 527.8, 23, 161),
            "BL_door": Item(7, 75.4, 527.8, -23, -161),
            "Rem_cyc": Item(0.6, 35.8, 21.48, -8, -4.8),
            "Rem_col": Item(0.8, 47, 37.6, -21, -16.8),
            "Rem_ped": Item(0.8, 12.8, 10.24, -9.5, -7.6),
            "Main_fuel": FuelTank(0, 106, 0, -13.5, 0, 29.5, 0),
            "Aux_fuel": FuelTank(0, 102, 0, 13, 0, 17, 0)
        }

        self._longitudinal_moment = 0
        self._longitudinal_arm = 0
        self._lateral_moment = 0
        self._lateral_arm = 0
        self._weight = 0

    def calculate_moments(self):
        for key in list(self._moments.keys()):
            if key == "empty":
                continue
            else:
                self._moments[key].calculate_moments()

    def calculate_com(self):
        sum_weight = 0
        sum_lat_moment = 0
        sum_lon_moment = 0
        for key, value in self._moments.items():
            sum_weight += value.get_weight()
            sum_lat_moment += value.get_lateral_moment()
            sum_lon_moment += value.get_longitudinal_moment()
        self._lateral_arm = sum_lat_moment / sum_weight
        self._longitudinal_arm = sum_lon_moment / sum_weight
        self._lateral_moment = sum_lat_moment
        self._longitudinal_moment = sum_lon_moment
        self._weight = sum_weight

    def set_weight(self, pos: str, weight: float) -> None:
        """
        Sets the weight of the item
        :param pos: The position you would like to set the desired weight to
        :param weight: The weight you would like to set the desried position to
        """
        try:
            self._moments[pos].set_weight(weight)
        except KeyError:
            raise R44.ItemNotInAircraftError("The item: {pos} does not exist in the aircraft".format(pos=pos))

    def set_vol(self, pos: str, vol: float) -> None:
        """
        Sets the volume of fuel of the given tank to the desired amount in gallons
        :param pos: The fuel tank you would like to set the volume
        :param vol: The volume of fuel you would like to calculated in gallons
        """
        try:
            self._moments[pos].set_vol(vol)
        except AttributeError:
            raise R44.ItemNotInAircraftError("The fuel tank {pos} does not exist in the aircraft".format(pos=pos))

    def __str__(self):
        s = ""
        for key, value in self._moments.items():
            s += "{name}: {info}\n".format(name = key, info = value)
        return s

    def __repr__(self):
        return self.__str__()