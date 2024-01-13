# Reading the File
with open('input_2.txt') as f:
    data = [i for i in f.read().split("\n")]

# print(data)

# part 1
score = 0

for item in data:
    if item == 'A X':
        score += 4
    elif item == 'A Y':
        score += 8
    elif item == 'A Z':
        score += 3
    elif item == 'B X':
        score += 1
    elif item == 'B Y':
        score += 5
    elif item == 'B Z':
        score += 9
    elif item == 'C X':
        score += 7
    elif item == 'C Y':
        score += 2
    elif item == 'C Z':
        score += 6

print(score)


# part 2
score2 = 0

for item in data:
    if item == 'A X':
        score2 += 3
    elif item == 'A Y':
        score2 += 4
    elif item == 'A Z':
        score2 += 8
    elif item == 'B X':
        score2 += 1
    elif item == 'B Y':
        score2 += 5
    elif item == 'B Z':
        score2 += 9
    elif item == 'C X':
        score2+= 2
    elif item == 'C Y':
        score2 += 6
    elif item == 'C Z':
        score2 += 7

print(score2)