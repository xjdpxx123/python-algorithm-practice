# x, n = map(int, input().split())

# kilometers = 0

# for i in range(n):
#     weekday = (x - 1 + i) % 7 + 1
#     """
#     原编号 1～7
#     先减 1，变成 0～6
#     做 % 7 循环
#     再加 1，变回 1～7
#     """

#     if weekday <= 5:
#         kilometers += 250

# print(kilometers)



x, n = map(int, input().split())

# 每个完整星期游 5 天
workdays = n // 7 * 5
remaining_days = n % 7

if remaining_days >= 1:
    if x <= 5:
        workdays += 1
    x = x % 7 + 1

if remaining_days >= 2:
    if x <= 5:
        workdays += 1
    x = x % 7 + 1

if remaining_days >= 3:
    if x <= 5:
        workdays += 1
    x = x % 7 + 1

if remaining_days >= 4:
    if x <= 5:
        workdays += 1
    x = x % 7 + 1

if remaining_days >= 5:
    if x <= 5:
        workdays += 1
    x = x % 7 + 1

if remaining_days >= 6:
    if x <= 5:
        workdays += 1

print(workdays * 250)