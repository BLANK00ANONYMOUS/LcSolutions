    class Solution:
        def maxMatrixSum(self, matrix: List[List[int]]) -> int:
            res = 0
            cnt = 0
            grMin = float("inf")

            for row in matrix:
                for n in row:
                    res += abs(n)
                    grMin = min(grMin, abs(n))
                    if n < 0:
                        cnt += 1

            if cnt & 1:
                res -= 2 * grMin

            return res