"""
1820. Maximum Number of Accepted Invitations
"""
class Solution:
    def maximumInvitations(self, grid: List[List[int]]) -> int:
        def dfs(node, seen):
            for neighbor in range(N):  # ask each girl
                if grid[node][neighbor] and not seen[neighbor]:
                    # a potential mate; the girl has not been asked before
                    seen[neighbor] = True  # mark her as asked
                    if matching[neighbor] == -1 or dfs(matching[neighbor], seen):
                        # if the girl does not have a mate or her mate can be matched to someone else
                        matching[neighbor] = node  # we match her to the boy "node"
                        return True
            return False

        M, N, ans = len(grid), len(grid[0]), 0
        matching = [-1] * N  # girls' mate
        for boy_index in range(M):
            if dfs(boy_index, [False] * N):
                ans += 1

        return ans
