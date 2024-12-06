class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cnt = defaultdict(int)

        for row in matrix:
            ky = str(row)

            if row[0]:
                ky = str([0 if n else 1 for n in row])

            cnt[ky] += 1

        return max(cnt.values())
