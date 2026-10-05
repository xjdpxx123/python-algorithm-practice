"""超时了！！！"""
# n, x = map(int, input().split())

# num_x = 0

# for i in range(1, n + 1):
#     num = i

#     while num > 0:
#         digit = num % 10 # 取出个位

#         if digit == x:
#             num_x += 1

#         num //= 10 # 删除个位

# print(num_x)

"""优化"""
n, x = map(int, input().split())

ans = 0
factor = 1  # 当前数位：1表示个位，10表示十位，100表示百位

while factor <= n:
    high = n // (factor * 10)   # 当前位左边的数字
    cur = (n // factor) % 10    # 当前位数字
    low = n % factor            # 当前位右边的数字

    if x != 0:
        if cur < x:
            ans += high * factor
        elif cur == x:
            ans += high * factor + low + 1
        else:
            ans += (high + 1) * factor

    else:
        # 统计0时不能把前导0计算进去
        if high == 0:
            break

        if cur == 0:
            ans += (high - 1) * factor + low + 1
        else:
            ans += high * factor

    factor *= 10

print(ans)