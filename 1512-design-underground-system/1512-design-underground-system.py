class UndergroundSystem:

    def __init__(self):
        self.checkedIn = {} #id -> (stationName,time)
        self.total = {} #(start,end) -> [total,count of element]
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.checkedIn[id] = (stationName , t)
        

    def checkOut(self, id: int, endStation: str, t: int) -> None:
        start , time = self.checkedIn[id]
        r = (start,endStation)

        if r not in self.total:
            self.total[r] = [0,0]
        
        self.total[r][0] += t - time
        self.total[r][1] += 1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total , count = self.total[(startStation,endStation)]
        return total / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)