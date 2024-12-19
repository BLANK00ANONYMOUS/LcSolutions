class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        cur_min = -1
        res = 0

        for i in range(len(arr) - 1, -1, -1):
            cur_min = min(arr[i], cur_min)

            if cur_min == i:
                res += 1

        return res