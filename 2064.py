class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def calc(x):
            stores = 0
            for q in quantities:
                stores += math.ceil(q / x)
            return stores <= n

        l, r = 1, max(quantities)
        res = 0
        while l <= r:
            mid = (l + r) // 2
            if calc(mid):
                r = mid - 1
                res = mid
            else:
                l = mid + 1

        return res

