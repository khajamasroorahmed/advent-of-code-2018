values = []
with open('input', 'r') as f:
    for line in f:
        values.append(line)
f.close()

#Part 1
count2 = 0
count3 = 0
for value in values:
    charDict = {}
    for char in value:
        if char in charDict:
            charDict[char] += 1
        else:
            charDict[char] = 1
    if 2 in charDict.values():
        count2 += 1
    if 3 in charDict.values():
        count3 += 1
print 'Checksum: ' + str(count2*count3)

#Part 2