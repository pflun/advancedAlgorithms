class Vehicle(object):
    def __init__(self):
        self.vid = 0
        self.size = 0
        self.ticketID = 0
        self.plate = 0

    def park(self, manager):
        pass

    def moveOut(self, manager):
        pass


class Motocycle(Vehicle):
    def __init__(self):
        super(Motocycle, self).__init__()
        self.size = 1


class Car(Vehicle):
    def __init__(self):
        super(Car, self).__init__()
        self.size = 2


class Bus(Vehicle):
    def __init__(self):
        super(Bus, self).__init__()
        self.size = 4


class Parkingspot(object):
    def __init__(self):
        self.psid = 0
        self.size = 0
        self.available = True


class Parkinglot(object):
    def __init__(self):
        self.plid = 0
        self.parkingspot = []


class Parkingticket(object):
    def __init__(self):
        self.tid = 0
        self.enterTime = 0
        self.leaveTime = 0
        self.plate = 0


class ParkingManager(object):
    def __init__(self):
        self.ticketList = []
        self.availableLots = []

    def findAvailable(self, size):
        pass

    def generateTicket(self, plate, enterTime, leaveTime):
        pass

    def withdrawTicket(self, tid):
        pass


test = Motocycle()
