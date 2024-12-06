class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        adj = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }

        b = "".join([str(c) for row in board for c in row])
        q = deque([(b.index("0"), b, 0)])
        visit = set([b])

        while q:
            i, b, length = q.popleft()

            if b == "123450":
                return length

            b_arr = list(b)
            for j in adj[i]:
                newArr = b_arr.copy()
                newArr[i], newArr[j] = b_arr[j], b_arr[i]
                newB = "".join(newArr)
                if newB not in visit:
                    q.append((j, newB, length + 1))
                    visit.add(newB)

        return -1

