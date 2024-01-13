# Reading the File
with open('input_4.txt') as f:
    data = [i for i in f.read().split("\n")]

# print(data)

# Parsing the Data
pair_1 = 0; pair_2 = 0

for item in data:
    x = item.split(',')
    str1 = x[0]
    str2 = x[1]

    a = [int(i) for i in str1.split('-')]
    b = [int(i) for i in str2.split('-')]

    print(a,b)

    # PART 1
    if a[0] <= b[0] and a[1] >= b[1]:
        pair_1 += 1
    elif a[0] >= b[0] and a[1] <= b[1]:
        pair_1 += 1

    # PART 2
    if a[1] >= b[0] and a[0] <= b[1]:
        pair_2 += 1

print(pair_1)
print(pair_2)