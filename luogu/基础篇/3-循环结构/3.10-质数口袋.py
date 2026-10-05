L = int(input())

number = 2 # 2是最小的质数
num = 0 # 记录number的因数个数
s = 0 # 记录质数口袋中的数字和
n = 0 # 记录质数口袋中质数的个数

while True:
    # 判断 number 是否是质数
    for i in range(2, number + 1):
        if number % i == 0:
            num += 1

    if num == 1:
        # 装入这个质数后会超重，就直接结束
        if s + number > L:
            break

        s += number
        n += 1
        print(number)

    number += 1
    num = 0

print(n)