"""
317. Shortest Distance from All Buildings
Hard

You are given an m x n grid grid of values 0, 1, or 2, where:

    each 0 marks an empty land that you can pass by freely,
    each 1 marks a building that you cannot pass through, and
    each 2 marks an obstacle that you cannot pass through.

You want to build a house on an empty land that reaches all buildings in the shortest total travel distance. You can only move up, down, left, and right.

Return the shortest travel distance for such a house. If it is not possible to build such a house according to the above rules, return -1.

The total travel distance is the sum of the distances between the houses of the friends and the meeting point.

The distance is calculated using Manhattan Distance, where distance(p1, p2) = |p2.x - p1.x| + |p2.y - p1.y|.

 

Example 1:

Input: grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
Output: 7
Explanation: Given three buildings at (0,0), (0,4), (2,2), and an obstacle at (0,2).
The point (1,2) is an ideal empty land to build a house, as the total travel distance of 3+3+1=7 is minimal.
So return 7.

Example 2:

Input: grid = [[1,0]]
Output: 1

Example 3:

Input: grid = [[1]]
Output: -1

 

Constraints:

    m == grid.length
    n == grid[i].length
    1 <= m, n <= 50
    grid[i][j] is either 0, 1, or 2.
    There will be at least one building in the grid.


"""


class Solution:
    def shortestDistance(self, grid: List[List[int]]) -> int:
        h = len(grid)
        w = len(grid[0])
        
        distance = [[0 for _ in range(w)] for _ in range(h)]
        reach = [[0 for _ in range(w)] for _ in range(h)]
        
        buildingNum = 0
        
        for i in range(h):
            for j in range(w
                          ):
                if grid[i][j] == 1:
                    buildingNum += 1
                    q = [(i, j, 0)]
                    
                    isVisited = [[False for _ in range(w)] for _ in range(h)]
                    
                    for y, x, d in q:
                        for dy, dx in (-1, 0), (1, 0), (0, -1), (0, 1):
                            r = y + dy
                            c = x + dx
                            
                            if 0 <= r < h and 0 <= c < w and grid[r][c] == 0 and not isVisited[r][c]:
                                distance[r][c] += d + 1
                                reach[r][c] += 1
                                
                                isVisited[r][c] = True
                                q.append((r, c, d + 1))
        
        shortest = float("inf")
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 0 and reach[i][j] == buildingNum:
                    shortest = min(shortest, distance[i][j])

        if shortest < float("inf"):
            return shortest
        else:
            return -1
        
        
