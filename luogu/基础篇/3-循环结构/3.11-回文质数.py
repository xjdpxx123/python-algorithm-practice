"""超时了！！！"""
# a,b = map(int,input().split())

# number = a
# num = 0 # 记录number的因数个数

# while number <= b:
#     # 判断 number 是否是质数
#     for i in range(2, number + 1):
#         if number % i == 0:
#             num += 1

#     if num == 1:
#         # # 判断回文数
#         # if str(number) == str(number)[::-1]:
#         #     print(number)

#         # 不使用字符串判断回文数
#         temp = number
#         reverse = 0

#         while temp > 0:
#             digit = temp % 10
#             reverse = reverse * 10 + digit
#             temp //= 10

#         if reverse == number:
#             print(number)

#     number += 1
#     num = 0

"""还是超时了！！！"""
# """优化，构造回文数，然后判断是否为质数"""
# a, b = map(int, input().split())

# left = 1

# while True:
#     number = left
#     temp = left // 10

#     # 构造回文数
#     while temp > 0:
#         number = number * 10 + temp % 10
#         temp //= 10

#     if number > b:
#         break

#     # 判断 number 是否是质数
#     if number >= a:
#         num = 0

#         for i in range(2, number + 1):
#             if number % i == 0:
#                 num += 1

#         if num == 1:
#             print(number)

#     if left == 9:
#         if a <= 11 <= b:
#             print(11)

#     left += 1

"""继续优化"""
a, b = map(int, input().split())

left = 5

while True:
    # 生成回文数
    number = left
    temp = left // 10

    while temp > 0:
        number = number * 10 + temp % 10
        temp //= 10

    if number > b:
        break

    # 判断质数
    if number >= a:
        # 先假设 number 是质数
        is_prime = 1

        # number 大于等于 5
        # 如果是偶数，就一定不是质数
        if number % 2 == 0:
            is_prime = 0
        else:
            # 只检查奇数因数
            i = 3

            # 只需要检查到 number 的平方根
            while i * i <= number:
                if number % i == 0:
                    is_prime = 0
                    break

                i += 2

        if is_prime == 1:
            print(number)

    # 当前方法无法生成两位回文数 11
    if left == 9 and a <= 11 <= b:
        print(11)

    left += 1