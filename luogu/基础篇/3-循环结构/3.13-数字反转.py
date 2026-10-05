N = int(input())

# 先处理负号
if N < 0:
    N = -N
    print("-", end="")

# 再处理数字反转
if N == 0:
    print(0)
else:
    started = False

    for _ in range(len(str(N))):
        digit = N % 10
        N //= 10

        if digit == 0 and not started:
            continue

        started = True
        print(digit, end="")