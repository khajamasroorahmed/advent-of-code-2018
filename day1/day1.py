import sys

values = []
total = 0
with open('input', 'r') as f:
    for line in f:
        values.append(int(line))
        total += int(line)
f.close()

# Part 1        
print 'Total: ' + str(total)

# Part 2
repeatedValueDict = {}
total = 0
while True:
    for value in values:
        total += value
        if total in repeatedValueDict:
            print 'Repeating Frequency: ' + str(total)
            sys.exit()
        else:
            repeatedValueDict[total] = 1