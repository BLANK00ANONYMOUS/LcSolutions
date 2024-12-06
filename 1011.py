class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        l, r = max(weights), sum(weights)
        res = r

        def good(mid):
            ships, currCap = 1, mid
            for w in weights:
                if currCap - w < 0:
                    ships += 1
                    currCap = mid
                currCap -= w
            return ships <= days

        while l <= r:
            mid = (l + r) // 2
            if good(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1

        return res
