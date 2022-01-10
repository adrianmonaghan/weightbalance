from aircrafts.item import Item
from aircrafts.item import FuelTank


class R44:

    class ItemNotInAircraftError(Exception):
        pass

    def __init__(self):
        self._moments = {
            "empty": Item(1466.2, 105.91, 155285.242, 0.31, 454.522, name="Basic Empty Weight", include=True),
            "FR_seat": Item(0, 49.5, 0, 12.2, 0, name="Front right seat pax weight", include=True),
            "FL_seat": Item(0, 49.5, 0, -10.4, 0, name="Front left seat pax weight", include=True),
            "FR_bag": Item(0, 44, 0, 11.5, 0, name="Front right seat baggage weight", include=True),
            "FL_bag": Item(0, 44, 0, -11.5, 0, name="Front left seat baggage weight", include=True),
            "BR_seat_bag": Item(0, 79.5, 0, 12.2, 0, name="Back right seat pax and bag weight", include=True),
            "BL_seat_bag": Item(0, 79.5, 0, -12.2, 0, name="Back left seat pax and bag weight", include=True),
            "FR_door": Item(7.5, 49.4, 370.5, 24, 180, name="Front right door included", bool_include=True),
            "FL_door": Item(7.5, 49.4, 370.5, -24, -180, name="Front left door included", bool_include=True),
            "BR_door": Item(7, 75.4, 527.8, 23, 161, name="Back right door included", bool_include=True),
            "BL_door": Item(7, 75.4, 527.8, -23, -161, name="Back left door included", bool_include=True),
            "Rem_cyc": Item(0.6, 35.8, 21.48, -8, -4.8, name="Removable cyclic included", bool_include=True),
            "Rem_col": Item(0.8, 47, 37.6, -21, -16.8, name="Removable collective included", bool_include=True),
            "Rem_ped": Item(0.8, 12.8, 10.24, -9.5, -7.6, name="Removable pedals included", bool_include=True),
            "Main_fuel": FuelTank(0, 106, 0, -13.5, 0, 29.5, 0, name="Volume of fuel in main tank (gal)", include=True),
            "Aux_fuel": FuelTank(0, 102, 0, 13, 0, 17, 0, name="Volume of fuel in aux tank (gal)", include=True)
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
        self.calculate_moments()
        sum_weight = 0
        sum_lat_moment = 0
        sum_lon_moment = 0
        for key, value in self._moments.items():
            if value.get_include():
                sum_weight += value.get_weight()
                sum_lat_moment += value.get_lateral_moment()
                sum_lon_moment += value.get_longitudinal_moment()
        self._lateral_arm = sum_lat_moment / sum_weight
        self._longitudinal_arm = sum_lon_moment / sum_weight
        self._lateral_moment = sum_lat_moment
        self._longitudinal_moment = sum_lon_moment
        self._weight = sum_weight

    def set_include(self, pos: str, include: bool) -> None:
        """
        Sets whether or not an item is included in the final calculation. I.E. whether or not to include a door. True
        if you would like to consider it in COM calcs, False if you would like to not consider
        :param pos: The position you would like to change the include to
        :param include: What you would like to change the position to include to
        """
        try:
            self._moments[pos].set_include(include)
        except KeyError:
            raise R44.ItemNotInAircraftError("The position {pos} does not exist in the R44".format(pos = pos))

    def set_value(self, pos: str, value: float) -> None:
        """
        Sets the value of the item to the desired amount. If its a weight item it sets the proper weight. If it is fuel
        tank, it says the desired volume
        :param pos: The position you would like to set the value to
        :param value: The value you would like to set the position to, either pounds or gallons
        """
        try:
            if isinstance(self._moments[pos], FuelTank):
                self._moments[pos].set_vol(value)
            else:
                self._moments[pos].set_weight(value)
        except KeyError:
            raise R44.ItemNotInAircraftError("The item: {pos} does not exist in the aircraft".format(pos=pos))

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

    def get_moments(self) -> dict:
        """
        Returns a dictionary of the internal names of the items as keys and the item objects as values.
        :return:
        """
        return self._moments

    def get_com(self) -> tuple:
        """
        Returns a dictionary of the center of mass information of the aircraft. Keys are: weight, longitudinal_arm,
        longitudinal_moment, lateral_arm, lateral_moment
        :return: A dictionary of the COM information
        """
        dct = {
            "weight": self._weight,
            "longitudinal_arm": self._longitudinal_arm,
            "longitudinal_moment": self._longitudinal_moment,
            "lateral_arm": self._lateral_arm,
            "lateral_moment": self._lateral_moment
        }
        return dct


    def get_com_info(self) -> str:
        """
        Converts all the center of mass information: Weight & lateral & longitudinal arm & moment to a string for output
        :return: A string with properly formatted information
        """
        return "Weight: {weight} | Long Arm {loa} | Long Mom {lom} | Lat Arm {laa} | Lat Mom {lam} | "\
            .format(weight=self._weight, loa=self._longitudinal_arm, lom=self._longitudinal_moment,
                    laa=self._lateral_arm, lam=self._lateral_moment)



    def __str__(self):
        s = ""
        for key, value in self._moments.items():
            s += "{name}: {info}\n".format(name = key, info = value)
        return s

    def __repr__(self):
        return self.__str__()