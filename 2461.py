class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        prev_idx = {}
        curr_sum = 0

        l = 0
        for r in range(len(nums)):
            curr_sum += nums[r]

            i = prev_idx.get(nums[r], -1)

            while l <= i or r - l + 1 > k:
                curr_sum -= nums[l]
                l += 1

            if r - l + 1 == k:
                res = max(res, curr_sum)

            prev_idx[nums[r]] = r

        return res
