class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        items.sort()
        queries = sorted[(q, i) for i, q in enumerate(queries)]

        res = [0] * len(queries)
        max_beu = 0
        j = 0

        for q, i in queries:
            while j < len(items) and items[j][0] <= q:
                max_beu = max(max_beu, items[j][i])
                j += 1

            res[i] = max_beu

        return res