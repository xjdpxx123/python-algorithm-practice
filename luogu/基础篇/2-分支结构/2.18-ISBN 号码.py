# isbn = input()

# total = (
#     int(isbn[0]) * 1
#     + int(isbn[2]) * 2
#     + int(isbn[3]) * 3
#     + int(isbn[4]) * 4
#     + int(isbn[6]) * 5
#     + int(isbn[7]) * 6
#     + int(isbn[8]) * 7
#     + int(isbn[9]) * 8
#     + int(isbn[10]) * 9
# )

# code = total % 11

# if code == 10:
#     correct_code = "X"
# else:
#     correct_code = str(code)

# if isbn[12] == correct_code:
#     print("Right")
# else:
#     print(isbn[:12] + correct_code)


# 不用字符串知识点
language, publisher, book, input_code = input().split("-")

language_number = int(language)
publisher_number = int(publisher)
book_number = int(book)

total = (
    language_number * 1
    + publisher_number // 100 * 2
    + publisher_number // 10 % 10 * 3
    + publisher_number % 10 * 4
    + book_number // 10000 * 5
    + book_number // 1000 % 10 * 6
    + book_number // 100 % 10 * 7
    + book_number // 10 % 10 * 8
    + book_number % 10 * 9
)

code = total % 11

if code == 10:
    correct_code = "X"
else:
    correct_code = str(code)

if input_code == correct_code:
    print("Right")
else:
    print(language, publisher, book, correct_code, sep="-")