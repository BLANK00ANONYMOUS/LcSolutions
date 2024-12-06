def minFlipsMonoIncr(s: str) -> int:
    cntZero = s.count('0')
    res = len(s)
    cnt = 0
    for i in range(len(s)):
        if s[i] == '0':
            cnt += 1
            res = min(res, i + 1 - 2 * cnt + cntZero)
    return res


k = input()
print(minFlipsMonoIncr(k))

