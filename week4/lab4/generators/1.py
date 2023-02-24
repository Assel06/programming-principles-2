def squares(a, n):
    while a < n:
        a += 1
        yield a*a
for i in squares(0, 20):
    print(i, end = " ")