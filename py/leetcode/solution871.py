from typing import List


class Solution:
    def minRefuelStops(self, target: int, startFuel: int, stations: List[List[int]]) -> int:
        """
        target = 100, startFuel = 10, stations = [[10,60],[20,30],[30,30],[60,40]]
        :param target:
        :param startFuel:
        :param stations:
        :return:
        """
        cnt = 0
        stations.sort(key=lambda x: x[0])
        last = -1
        prevList = []
        for (k,v) in enumerate(stations):
            startFuel = startFuel - v[0]
            if startFuel > 0:
                prevList.append(v)
                continue
            else:
                for i in prevList:
                    
