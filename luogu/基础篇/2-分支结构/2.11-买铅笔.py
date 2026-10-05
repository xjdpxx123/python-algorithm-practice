# n = int(input())

# price_total = 10**100  # 先设成一个很大的数

# for i in range(3):
#     num, price = map(int, input().split())

#     # 购买这种包装需要花的钱
#     current_price = (n + num - 1) // num * price

#     # 保留目前最小的花费
#     if current_price < price_total:
#         price_total = current_price

# print(price_total)


n = int(input())

num1, price1 = map(int, input().split())
num2, price2 = map(int, input().split())
num3, price3 = map(int, input().split())

cost1 = (n + num1 - 1) // num1 * price1
cost2 = (n + num2 - 1) // num2 * price2
cost3 = (n + num3 - 1) // num3 * price3

answer = cost1

if cost2 < answer:
    answer = cost2

if cost3 < answer:
    answer = cost3

print(answer)