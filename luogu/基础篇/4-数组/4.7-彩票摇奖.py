n = int(input())

winning_numbers = list(map(int, input().split()))

prizes = [0] * 7

for i in range(n):
    match_count = 0

    numbers = list(map(int, input().split()))

    for j in range(len(numbers)):
        if numbers[j] in winning_numbers:
            match_count += 1

    if match_count == 0:
        continue

    prizes[7 - match_count] += 1

print(*prizes)