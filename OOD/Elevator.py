class Elevator(object):
    def __init__(self):
        self.currFloor = 0
        self.maxFloor = 0
        self.minFloor = 0
        self.direction = ''
        # stop or not
        self.state = 0
        self.doorState = 0
        self.maxWeight = 0
        self.queue = []

    def goToFloor(self):
        pass

    def openDoor(self):
        pass

class controller(object):
    def __init__(self):
        self.currFloor = 0
        self.elevatorDirection = ''

    def showCurrFloor(self):
        pass

class innerController(controller):
    def __init__(self):
        super(innerController, self).__init__()
        self.btn = ['up', 'down']

class outerController(controller):
    def __init__(self):
        super(outerController, self).__init__()
        self.btn = [1, 2, 3, 4, 5, 6, 7, 8]