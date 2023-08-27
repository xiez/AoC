# source: https://adventofcode.com/2021/day/1

# part 1
loi = []                      # list of integers
with open('./input') as f:
    for ln in f:
        loi.append(int(ln))

def count(lines):
    counter = 0
    prev_depth = lines[0]
    for depth in lines[1:]:
        if depth > prev_depth:
            # print(f'{depth} > {prev_depth}, increase counter')
            counter += 1
        prev_depth = depth
    return counter

print('How many measurements are larger than the previous measurement?')
print('Answers:', count(loi))

# part 2 -- naive
los = []                        # list of sums
try:
    for idx, i in enumerate(loi):
        los.append(sum([i, loi[idx + 1], loi[idx + 2]]))
except IndexError:
    pass

print('Consider sums of a three-measurement sliding window. How many sums are larger than the previous sum?')
print('Answer:', count(los))

# part2 -- slightly improved
step = 3                        # slide window size
los = []                        # list of sums
len_loi = len(loi)
for idx, _ in enumerate(loi):
    if idx == (len_loi - (step - 1)):
        break
    los.append(sum(loi[idx: idx + step]))

def count2(lines):
    return sum(
        [1 if next > prev else 0 for prev, next in zip(lines, lines[1:])]
    )

print('Answer2:', count2(los))
