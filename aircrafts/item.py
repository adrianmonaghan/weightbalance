class Item:

    def __init__(self, weight: float = 0, longitudinal_arm: float = 0, longitudinal_moment: float = 0,
                 lateral_arm: float = 0, lateral_moment: float = 0, minimum: float = 0, maximum: float = 0) -> object:
        """
        :rtype: object
        :param weight: Weight in pounds
        :param longitudinal_arm: Longitudinal arm in inches
        :param longitudinal_moment: Longitudinal moment in pound inches
        :param lateral_arm: Lateral arm in inches
        :param lateral_moment: Lateral moment in pound inches
        """
        self._weight = weight
        self._longitudinal_arm = longitudinal_arm
        self._longitudinal_moment = longitudinal_moment
        self._lateral_arm = lateral_arm
        self._lateral_moment = lateral_moment

    def calculate_moments(self) -> None:
        """
        Calculates the lateral and longitudinal moments and stores them in the object
        :rtype: None
        """
        self._longitudinal_moment = round(self._weight * self._longitudinal_arm, 5)
        self._lateral_moment = round(self._weight * self._lateral_arm, 5)

    def set_weight(self, weight: float) -> None:
        """
        Sets the weight to a desired amount
        :rtype: None
        :param weight: Weight in pounds
        """
        self._weight = weight

    def get_weight(self) -> float:
        """
        :return: The weight of the item
        """
        return self._weight

    def get_longitudinal_moment(self) -> float:
        """
        :return: The longitudinal moment of the item
        """
        return self._longitudinal_moment

    def get_lateral_moment(self) -> float:
        """
        :return: The lateral moment of the item
        """
        return self._lateral_moment

    def __iter__(self):
        lst = [self._weight, self._longitudinal_arm, self._longitudinal_moment, self._lateral_arm, self._lateral_moment]
        return iter(lst)

    def __str__(self):
        return "Weight: {0} | Long Arm {1} | Long Mom {2} | Lat Arm {3} | Lat Mom {4}".format(*tuple(self))

    def __repr__(self):
        return self.__str__()


class FuelTank(Item):

    class TooMuchFuelError(Exception):
        pass

    def __init__(self, weight: float = 0, longitudinal_arm: float = 0, longitudinal_moment: float = 0,
                 lateral_arm: float = 0, lateral_moment: float = 0, max_fuel_vol: float = 0,
                 fuel_vol: float = 0) -> object:
        """
        :rtype: object
        :param weight: Weight in pounds
        :param longitudinal_arm: Longitudinal arm in inches
        :param longitudinal_moment: Longitudinal moment in pound inches
        :param lateral_arm: Lateral arm in inches
        :param lateral_moment: Lateral moment in pound inches
        :param max_fuel_vol: Maximum fuel volume in gallons
        :param fuel_vol: Fuel volume in gallons
        """
        super().__init__(weight, longitudinal_arm, longitudinal_moment, lateral_arm, lateral_moment)
        self._max_fuel_vol = max_fuel_vol
        self._fuel_vol = fuel_vol

    def calculate_moments(self) -> None:
        """
        Calculates the lat and lon moments for the fuel tank
        :rtype: None
        """
        self.vol_to_pounds()
        super().calculate_moments()

    def set_vol(self, vol: float) -> None:
        """
        Sets the volume to the desired amount in gallons
        :param vol: The volume of fuel you would like to calculate in gallons
        """
        if vol > self._max_fuel_vol:
            raise FuelTank.TooMuchFuelError("The volume of {v} gallons is larger than maximum amount of allowed fuel: "
                                            "{m}".format(v=vol, m=self._max_fuel_vol))
        else:
            self._fuel_vol = vol

    def vol_to_pounds(self) -> float:
        """
        Calculates and returns the weight of the fuel in the tank
        :rtype: float
        :return: The weight of the fuel in pounds
        """
        self.set_weight(self._fuel_vol * 6)
        return self._weight

    def __str__(self):
        return super().__str__() + " | Max Fuel Vol: {0} | Fuel Vol: {1}".format(self._max_fuel_vol, self._fuel_vol)

    def __repr__(self):
        return self.__str__()