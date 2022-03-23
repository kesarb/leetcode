"""
210. Course Schedule II
Medium

6332

231

Add to List

Share
There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.

 

Example 1:

Input: numCourses = 2, prerequisites = [[1,0]]
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So the correct course order is [0,1].
Example 2:

Input: numCourses = 4, prerequisites = [[1,0],[2,0],[3,1],[3,2]]
Output: [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3].
Example 3:

Input: numCourses = 1, prerequisites = []
Output: [0]
 

Constraints:

1 <= numCourses <= 2000
0 <= prerequisites.length <= numCourses * (numCourses - 1)
prerequisites[i].length == 2
0 <= ai, bi < numCourses
ai != bi
All the pairs [ai, bi] are distinct.
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
                        
        return res if len(res) == numCourses else [] 
                
    def dfs(self, numCourses, prerequisites):
        g = {}
        
        for a,b in prerequisites:
            if b not in g:
                g[b] = []
            g[b].append(a)
            
        #print( g)
        visit = set()
        cycle = set()
        res =[]
        def rec(curr, visit, cycle):
            if curr in visit:
                return True
            
            if curr in cycle:
                return False
                
            cycle.add(curr)
            if curr in g:
                for each in g[curr]:
                    if rec(each, visit, cycle) == False:
                        return False

            res.append(curr)
            visit.add(curr)
            cycle.remove(curr)
            return True
        
        for each in range(numCourses):
            if each not in visit and not rec(each, visit, cycle):
                return []
        
        return res and res[::-1]
    
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        #return self.indegree(numCourses, prerequisites)
        return self.dfs(numCourses, prerequisites)
