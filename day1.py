# Day 1
# Part One

from itertools import pairwise

read_file = open('input.txt', 'r', encoding='utf-8')
sweep = list(map(int,read_file.read().split('\n')))
count = 0
for (first, second) in pairwise(sweep):
    if second > first:
        count += 1
print(" Part One: " + str(count))

# Part Two

read_file = open('input.txt', 'r', encoding='utf-8')
sweep = list(map(int,read_file.read().split('\n')))
count = 0
s_len = len(sweep)
for num in range(0, s_len-3):
    first = sweep[num] + sweep[num + 1] + sweep[num + 2]
    second = sweep[num + 1] + sweep[num + 2] + sweep[num + 3]
    if second > first:
        count += 1

print(" Part Two: " + str(count))

