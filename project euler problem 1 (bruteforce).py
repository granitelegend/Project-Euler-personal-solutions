# Project Euler Problem 1

multiplesList = []

intList = list(range(1, 1000))

for x in intList:
    if x % 3 == 0 or x % 5 == 0:
        multiplesList.append(x)
        continue
    else:
        continue

print(sum(multiplesList))
