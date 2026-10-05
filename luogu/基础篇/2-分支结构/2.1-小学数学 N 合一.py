# import sys
# # 填上你觉得需要的其他模块

# def main():
#     T = int(input())
#     if T == 1:
#         print("I love Luogu!")
#     elif T == 2:
#         print(2 + 4, 10 - 2 - 4)
#     elif T == 3:
#         print(14 // 4, 14 // 4 * 4, 14 % 4, sep="\n")
#     elif T == 4:
#         print(f"{500 / 3:.6g}") # g 保留有效数字
#     elif T == 5:
#         print(int((260 + 220) / (12 + 20)))
#     elif T == 6:
#         print(f"{(9 ** 2 + 6 ** 2) ** 0.5:.6g}")
#     elif T == 7:
#         print(100+10, 100+10-20, 0, sep="\n")
#     elif T == 8:
#         print(f"{2 * 3.141593 * 5:.6g}", f"{3.141593 * 5 ** 2:.6g}", f"{4 / 3 * 3.141593 * 5 ** 3:.6g}", sep="\n")
#     elif T == 9:
#         # ((x / 2 - 1) / 2 - 1) / 2 - 1 = 1
#         print(22)
#     elif T == 10:
#         # x：原有任务
#         # y：每分钟增加
#         # x + 30y = 240
#         # x + 6y = 60
#         print(9)
#     elif T == 11:
#         print(f"{100 / (8 - 5):.6g}")
#     elif T == 12:
#         print(ord('M') - ord('A') + 1, chr(ord('A') + 18 - 1), sep="\n")
#     elif T == 13:
#         V = 4 / 3 * 3.141593 * (4**3+10**3)
#         print(int(V ** (1 / 3)))
#     elif T == 14:
#         # (110-x) * (10+x) = 3500
#         print(50)

# if __name__ == "__main__":
#     main()

T = int(input())
if T == 1:
    print("I love Luogu!")
elif T == 2:
    print(2 + 4, 10 - 2 - 4)
elif T == 3:
    print(14 // 4, 14 // 4 * 4, 14 % 4, sep="\n")
elif T == 4:
    print(f"{500 / 3:.6g}") # g 保留有效数字
elif T == 5:
    print(int((260 + 220) / (12 + 20)))
elif T == 6:
    print(f"{(9 ** 2 + 6 ** 2) ** 0.5:.6g}")
elif T == 7:
    print(100+10, 100+10-20, 0, sep="\n")
elif T == 8:
    print(f"{2 * 3.141593 * 5:.6g}", f"{3.141593 * 5 ** 2:.6g}", f"{4 / 3 * 3.141593 * 5 ** 3:.6g}", sep="\n")
elif T == 9:
    # ((x / 2 - 1) / 2 - 1) / 2 - 1 = 1
    print(22)
elif T == 10:
    # x：原有任务
    # y：每分钟增加
    # x + 30y = 240
    # x + 6y = 60
    print(9)
elif T == 11:
    print(f"{100 / (8 - 5):.6g}")
elif T == 12:
    print(ord('M') - ord('A') + 1, chr(ord('A') + 18 - 1), sep="\n")
elif T == 13:
    V = 4 / 3 * 3.141593 * (4**3+10**3)
    print(int(V ** (1 / 3)))
elif T == 14:
    # (110-x) * (10+x) = 3500
    print(50)
