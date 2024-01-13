# Reading the File
with open('input_3.txt') as f:
    data = [i for i in f.read().split("\n")]

# print(data,len(data))

# PART 1 - Finding common character from two halves of a given string
# Defining the values
list1 = []
# list2 = [] - used in a code which didn't give correct values 
score = 0
Dict = {
    "a":1, "b":2, "c":3, "d":4, "e":5, "f":6, "g":7, "h":8, "i":9, "j":10, 
    "k":11, "l":12, "m":13, "n":14, "o":15, "p":16, "q":17, "r":18, "s":19, "t":20, 
    "u":21, "v":22, "w":23, "x":24, "y":25, "z":26, "A":27, "B":28, "C":29, "D":30, 
    "E":31, "F":32, "G":33, "H":34, "I":35, "J":36, "K":37, "L":38, "M":39, "N":40, 
    "O":41, "P":42, "Q":43, "R":44, "S":45, "T":46, "U":47, "V":48, "W":49, "X":50, 
    "Y":51, "Z":52
}

for item in data:
    half = len(item)//2
    str1 = item[:half]
    str2 = item[half:]
    for i in Dict:
        if i in str1 and i in str2:
            # list2.append(i)
            score += Dict[i]

# print(len(list2)) - Used to check for unecessary values in list
print(score)

# PART 2 - Finding a common character between a bunch of 3 strings
score1 = 0

for j in range(0,len(data),3):
    str1 = data[j]
    str2 = data[j+1]
    str3 = data[j+2]
    
    for i in Dict:
        if i in str1 and i in str2 and i in str3:
            score1 += Dict[i]

print(score1)