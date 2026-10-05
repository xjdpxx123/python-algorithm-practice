m, t, s = map(int, input().split())

if t == 0:
    print(0)
else:
    apple = m - (s + t - 1) // t

    if apple < 0:
        apple = 0

    print(apple)