from collections import defaultdict
from typing import List


class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        adj = defaultdict(list)
        for src, dst, dist in roads:
            adj[src].append((dst, dist))
            adj[dst].append((src, dist))


        def dfs(node):
            if node in visit:
                return
            visit.add(node)
            nonlocal res
            for neigh, dist in adj[node]:
                res = min(res, dist)
                dfs(neigh)

        visit = set()
        res = float("inf")
        dfs(1)
        return res