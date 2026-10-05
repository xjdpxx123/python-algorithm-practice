k = int(input())

coin = 1       # 当前每天发几枚金币
used_day = 0   # 当前档位已经发了多少天
total = 0      # 金币总数

for day in range(1, k + 1):
    total += coin
    used_day += 1

    # 当前档位已经发够 coin 天
    if used_day == coin:
        coin += 1
        used_day = 0

print(total)