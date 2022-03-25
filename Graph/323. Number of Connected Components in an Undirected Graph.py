"""
323. Number of Connected Components in an Undirected Graph
Medium

You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates that there is an edge between ai and bi in the graph.

Return the number of connected components in the graph.

 

Example 1:

Input: n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:

Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

 

Constraints:

    1 <= n <= 2000
    1 <= edges.length <= 5000
    edges[i].length == 2
    0 <= ai <= bi < n
    ai != bi
    There are no repeated edges.


"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        visit = set()
        parents={}
        dict_set = defaultdict(set)
        latest = None
        for v1,v2 in edges:
            #print(parents, dict_set)
            visit.add(v1)
            visit.add(v2)
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
                d1 = a
                if len(first) > len(second):
                    p = a
                    d1 = b
                    first = dict_set[b]
                    second = dict_set[a]
                for each in first:
                    second.add(each)
                    parents[each]=p
                
                first.clear()
                del dict_set[d1]
                
        return len(dict_set)+(n-len(visit))
        
