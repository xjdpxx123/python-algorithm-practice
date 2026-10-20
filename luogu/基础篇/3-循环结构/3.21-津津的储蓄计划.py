money = 0
save = 0
flag = 0

for i in range(1, 13):
    x = int(input())

    money += 300

    if money < x:
        flag = i
        break

    money -= x

    a = money // 100 * 100
    save += a
    money -= a

if flag != 0:
    print(-flag)
else:
    print(int(money + save * 1.2))