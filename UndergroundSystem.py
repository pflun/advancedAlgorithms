class UndergroundSystem(object):

    def __init__(self):
        # start => {end => [total time, total ride]}
        self.avg = {}
        # id => [start station, start t]
        self.ride = {}

    def checkIn(self, id, stationName, t):
        if id in self.ride:
            return -1
        self.ride[id] = [stationName, t]

    def checkOut(self, id, stationName, t):
        if id not in self.ride:
            return -1
        startStation = self.ride[id][0]
        startT = self.ride[id][1]
        del self.ride[id]
        if startStation in self.avg:
            if stationName in self.avg[startStation]:
                prevTime = self.avg[startStation][stationName][0]
                prevRide = self.avg[startStation][stationName][1]
                self.avg[startStation][stationName] = [prevTime + t - startT, prevRide + 1]
            else:
                self.avg[startStation][stationName] = [t - startT, 1]
        else:
            self.avg[startStation] = {}
            self.avg[startStation][stationName] = [t - startT, 1]

    def getAverageTime(self, startStation, endStation):
        if startStation in self.avg:
            totalTime = self.avg[startStation][endStation][0]
            totalRide = self.avg[startStation][endStation][1]
            return totalTime / float(totalRide)

test = UndergroundSystem()
test.checkIn(45, "Leyton", 3)
test.checkIn(32, "Paradise", 8)
test.checkIn(27, "Leyton", 10)
test.checkOut(45, "Waterloo", 15)
test.checkOut(27, "Waterloo", 20)
test.checkOut(32, "Cambridge", 22)
print test.getAverageTime("Paradise", "Cambridge")
print test.getAverageTime("Leyton", "Waterloo")
test.checkIn(10, "Leyton", 24)
print test.getAverageTime("Leyton", "Waterloo")
test.checkOut(10, "Waterloo", 38)
print test.getAverageTime("Leyton", "Waterloo")