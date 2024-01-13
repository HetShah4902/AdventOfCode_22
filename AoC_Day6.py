# Reading the File
with open('input_6.txt') as f:
    data = f.read()

# print(data)

# PART 1 
for i in range(0,len(data)-3):
    str1 = set(data[i:i+4])
    # print(str1,i+4)
    if len(str1) == 4:
        print(i+4)
        break

# PART 2 - just change all values of 4 to 14
for i in range(0,len(data)-13):
    str1 = set(data[i:i+14])
    # print(str1,i+14)
    if len(str1) == 14:
        print(i+14)
        break