class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [cost[0], cost[1]]

        for i in range(2, len(cost)):
            k = cost[i] + min(dp[i - 1], dp[i - 2])
            dp.append(k)

        return min(dp[len(cost) - 1], dp[len(cost) - 2])