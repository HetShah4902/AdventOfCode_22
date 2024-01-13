# Reading the File
with open('input_1.txt') as f:
    data = [i for i in f.read().split("\n")]

# print(data)

# Defining the values
calorie = 0
max = 0
allcal = []

# Traversing the data
for item in data:
    if item == '':
        calorie = 0
    else:
        num = int(item)
        calorie += num 
        allcal.append(calorie) # creating a list to gather all values of calories

    if calorie > max:
        max = calorie

# Sorting calorie values to get largest 3 values
allcal.sort()
a = allcal[-1]
b = allcal[-2]
c = allcal[-3]

# part1
print(max)
# part2
print(a+b+c)