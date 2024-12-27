class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = defaultdict(int)

        dp[0] = 1

        for i in range(len(nums)):
            num_dp = defaultdict(int)
            for cur_sum, count in dp.items():
                num_dp[cur_sum + nums[i]] += count
                num_dp[cur_sum - nums[i]] += count
            dp = num_dp
        return dp[target]
