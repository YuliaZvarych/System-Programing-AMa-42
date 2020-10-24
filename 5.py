def paper_cut(n, m):
    if n == m:
        return 1
    c = 0
    while n > 0 and m > 0:
        c += 1
        if m > n:
            n, m = m, n
        n, m = m, n-m
    return c


print(paper_cut(4, 5))
