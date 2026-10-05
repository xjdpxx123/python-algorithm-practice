# max_time = 8
# answer = 0

# for i in range(7):
#     school, mother = map(int, input().split())
#     total = school + mother

#     if total > max_time:
#         max_time = total
#         answer = i + 1

# print(answer)


max_time = 8
answer = 0

# 周一
school, mother = map(int, input().split())
total = school + mother
if total > max_time:
    max_time = total
    answer = 1

# 周二
school, mother = map(int, input().split())
total = school + mother
if total > max_time:
    max_time = total
    answer = 2

# 周三
school, mother = map(int, input().split())
total = school + mother
if total > max_time:
    max_time = total
    answer = 3

# 周四
school, mother = map(int, input().split())
total = school + mother
if total > max_time:
    max_time = total
    answer = 4

# 周五
school, mother = map(int, input().split())
total = school + mother
if total > max_time:
    max_time = total
    answer = 5

# 周六
school, mother = map(int, input().split())
total = school + mother
if total > max_time:
    max_time = total
    answer = 6

# 周日
school, mother = map(int, input().split())
total = school + mother
if total > max_time:
    max_time = total
    answer = 7

print(answer)