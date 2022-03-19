
"""
399. Evaluate Division
Medium

You are given an array of variable pairs equations and an array of real numbers values, where equations[i] = [Ai, Bi] and values[i] represent the equation Ai / Bi = values[i]. Each Ai or Bi is a string that represents a single variable.

You are also given some queries, where queries[j] = [Cj, Dj] represents the jth query where you must find the answer for Cj / Dj = ?.

Return the answers to all queries. If a single answer cannot be determined, return -1.0.

Note: The input is always valid. You may assume that evaluating the queries will not result in division by zero and that there is no contradiction.

 

Example 1:

Input: equations = [["a","b"],["b","c"]], values = [2.0,3.0], queries = [["a","c"],["b","a"],["a","e"],["a","a"],["x","x"]]
Output: [6.00000,0.50000,-1.00000,1.00000,-1.00000]
Explanation: 
Given: a / b = 2.0, b / c = 3.0
queries are: a / c = ?, b / a = ?, a / e = ?, a / a = ?, x / x = ?
return: [6.0, 0.5, -1.0, 1.0, -1.0 ]

Example 2:

Input: equations = [["a","b"],["b","c"],["bc","cd"]], values = [1.5,2.5,5.0], queries = [["a","c"],["c","b"],["bc","cd"],["cd","bc"]]
Output: [3.75000,0.40000,5.00000,0.20000]

Example 3:

Input: equations = [["a","b"]], values = [0.5], queries = [["a","b"],["b","a"],["a","c"],["x","y"]]
Output: [0.50000,2.00000,-1.00000,-1.00000]

"""

from collections import defaultdict

class Solution:
    def calcEquation(self, e: List[List[str]], v: List[float], q: List[List[str]]) -> List[float]:
        
        g = defaultdict(dict)
        
        for i in range(len(e)):
            A = e[i][0]
            B = e[i][1]
            g[A][B] = v[i]
            g[B][A] = 1/v[i]
            
        
        def dfs(x, y, visited):
            if x not in g or y not in g:
                return -1.0
            
            if y in g[x]:
                return g[x][y]
            
            for each in g[x]:
                if each not in visited:
                    visited[each] = 1
                    t = dfs(each, y, visited)
                    visited[each] = 0
                    if t != -1.0:
                        return g[x][each] * t
            return -1.0
        
        res = []
        for e1, e2 in q:
            res.append(dfs(e1, e2, {}))
        return res
