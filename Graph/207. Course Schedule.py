"""
207. Course Schedule
Medium

8804

354

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return true if you can finish all courses. Otherwise, return false.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: true
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
To take course 1 you should have finished course 0, and to take course 0 you should also have finished course 1. So it is impossible.
 

Constraints:

1 <= numCourses <= 105
0 <= prerequisites.length <= 5000
prerequisites[i].length == 2
0 <= ai, bi < numCourses
All the pairs prerequisites[i] are unique.
"""

class Solution:
    def indegree(self, numCourses, prerequisites):
        g = {}
        indegree = [0]*numCourses
        
        for a,b in prerequisites:
            if b not in g:
                g[b] = []
            g[b].append(a)
            indegree[a] += 1
        #print(indegree, g)
        queue = []
        res = []
        for index, val in enumerate(indegree):
            if val == 0:
                queue.append(index)    
            
        while queue:
            u = queue.pop(0)
            #print(u)
            res.append(u)
            if u in g:
                for each in g[u]:
                    indegree[each] -= 1
                    if indegree[each] == 0:
                        queue.append(each)
        return len(res) == numCourses
                
    def dfs(self, numCourses, prerequisites):
        g = {}
        
        for a,b in prerequisites:
            if b not in g:
                g[b] = []
            g[b].append(a)
            
        #print( g)
        visit = set()
        cycle = set()
        
        def rec(curr, visit, cycle):
            if curr in visit or curr not in g:
                return True
            
            if curr in cycle:
                return False
                
            cycle.add(curr)
            
            for each in g[curr]:
                if rec(each, visit, cycle) == False:
                    return False
            
            visit.add(curr)
            cycle.remove(curr)
            return True
        
        for each in g:
            if each not in visit and not rec(each, visit, cycle):
                return False
            
        return True
        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        #return self.indegree(numCourses, prerequisites)
        return self.dfs(numCourses, prerequisites)
      
