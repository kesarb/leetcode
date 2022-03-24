"""
684. Redundant Connection

In this problem, a tree is an undirected graph that is connected and has no cycles.

You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.

 

Example 1:


Input: edges = [[1,2],[1,3],[2,3]]
Output: [2,3]
Example 2:


Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
Output: [1,4]
 

Constraints:

n == edges.length
3 <= n <= 1000
edges[i].length == 2
1 <= ai < bi <= edges.length
ai != bi
There are no repeated edges.
The given graph is connected.
"""

from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parents={}
        dict_set = defaultdict(set)
        latest = None
        for v1,v2 in edges:
            #print(parents, dict_set)
            a=parents.get(v1, -1)
            b= parents.get(v2, -1)
            if a==b and a != -1:
                latest = [v1,v2]
                continue
                
            if a ==-1 and b != -1:
                parents[v1]=b
                dict_set[b].add(v1)
            elif a !=-1 and b == -1:
                parents[v2]=a
                dict_set[a].add(v2)
            elif a == -1 and b == -1:
                dict_set[v1].add(v1)
                dict_set[v1].add(v2)
                parents[v1]=v1
                parents[v2]=v1
            else:
                first = dict_set[a]
                second = dict_set[b]
                p = b
                if len(first) > len(second):
                    p = a
                    first = dict_set[b]
                    second = dict_set[a]
                for each in first:
                    second.add(each)
                    parents[each]=p
                
                first.clear()
        return latest
                
