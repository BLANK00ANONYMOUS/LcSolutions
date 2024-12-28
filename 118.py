class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1, numRows - 1):
            dp = res[-1]
            curr_dp = [1]
            for j in range(1, len(dp)):
                curr_dp.append(dp[j] + dp[j - 1])
            res.append(curr_dp)

        return res