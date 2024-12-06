from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        remain = total % p

        if remain == 0:
            return 0

        res = len(nums)
        cur_sum = 0
        rem_pref = {
            0: -1
        }
        for i, n in enumerate(nums):
            cur_sum = (cur_sum + n) % p
            pref = (cur_sum - remain + p) % p
            if pref in rem_pref:
                x = i - rem_pref[pref]
                res = min(res, x)
            rem_pref[cur_sum] = i

        return -1 if res == len(nums) else res
