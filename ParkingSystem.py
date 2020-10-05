class ParkingSystem(object):

    def __init__(self, big, medium, small):
        """
        :type big: int
        :type medium: int
        :type small: int
        """
        self.garage = [big, medium, small]

    def addCar(self, carType):
        """
        :type carType: int
        :rtype: bool
        """
        carType = carType - 1
        if self.garage[carType] == 0:
            return False
        else:
            self.garage[carType] -= 1
            return True