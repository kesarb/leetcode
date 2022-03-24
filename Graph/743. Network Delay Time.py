"""
743. Network Delay Time
Medium

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

 

Example 1:


Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2
Example 2:

Input: times = [[1,2,1]], n = 2, k = 1
Output: 1
Example 3:

Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 

Constraints:

1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

import heapq
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        max_int = float("inf")
        
        g = [[] for i in range(0, n+1)]
        
        for i, j, w in times:
            g[i].append([j,w])
            
        dist = [max_int]*(n+1)
        
        visit = set()
        
        
        # Dijkstra algorithm applied
        # initially all the nodes having max distance
        # pick the source node ele and make distance is zero and push into the prioirty queue
        # while queue is not empty
        # pop the priority queue element
        # do the BFS and push into Queue is it not already discovered 
        # return the max distance
        heap = [(0, k)]
        
        heapq.heapify(heap)
        dist[k] = 0
        
        while heap:
            d, node = heapq.heappop(heap)
            if node not in visit:
                dist[node] = d
                visit.add(node)
                for new_node, w in g[node]:
                    if new_node not in visit:
                        heapq.heappush(heap, (d+w, new_node))
                
        t = max(dist[1:])
        return -1 if t== max_int else t
