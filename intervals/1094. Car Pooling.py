"""
1094. Car Pooling
Medium

2944

64

Add to List

Share
There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trips[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.
"""

class Solution:
    def carPooling1(self, trips: List[List[int]], capacity: int) -> bool:
        trips.sort(key = lambda x: (x[1],x[2],x[0]))
        heap = []
        rooms = 0
        cap = 0
        for cum, From, to in trips:
            while heap and heap[0][0] <= From:
                x = heapq.heappop(heap)
                cap -= x[2]
            if cap + cum <= capacity:
                heapq.heappush(heap, (to,From, cum))
                cap += cum
            else:
                return False
        return True
    
    def carPooling(self, trips, capacity):
        ctr = 0
        expand  = []
        for p, i, j in trips:
            expand.append((i,p))
            expand.append((j,-1*p))
        expand.sort()
        minimum = 0
        for i,j in expand:
            ctr += j
            if ctr > capacity:
                return False
        return True
