class OOElevator(object):
    def __init__(self, id, currFloor, maxFloor, mode):
        self.id = id
        self.currFloor = currFloor
        self.maxFloor = maxFloor
        self.mode = mode  # enum
        self.destinations = []

    def move(self):
        if len(self.destinations) == 0:
            return

        while self.destinations:
            if self.destinations[0] > self.currFloor and self.mode != Stay.down:
                self.mode = Stay.up
                self.currFloor = self.destinations.pop(0)
            elif self.destinations[0] < self.currFloor and self.mode != Stay.up:
                self.mode = Stay.down
                self.currFloor = self.destinations.pop(0)
            else:
                self.mode = State.stay

    def pressBtn(self, floor):
        self.destinations.append(floor)


class State(enum.Enum):
    up = 1
    down = 2
    stay = 3
