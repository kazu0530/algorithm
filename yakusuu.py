def calc_divisor(n: int) -> List[int]:
    res = []
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            res.append(i)
            j = n // i
            if j != i:
                res.append(j)
    res.sort()
    return res

N, M = map(int, input().split())
div = calc_divisor(M)

# M の約数 d であって、d * N <= M となる最大の d を求める
res = 1
for d in div:
    if d * N <= M:
        res = max(res, d)

print(res)
