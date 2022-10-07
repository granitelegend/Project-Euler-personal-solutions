# Project Euler Problem 2

#  Instead of generating all Fibonacci numbers and then checking for even numbers
#  Checking and generating will happen at the same time

#  The algorithm

evenfiboList = []
fiboList = [0, 1]
n1 = 0
n2 = 1
nth = 0
while nth < 4 * (10 ** 6):
    nth = n1 + n2
    n1 = n2
    n2 = nth
    if nth % 2 == 0:
        evenfiboList.append(nth)
        continue

print(evenfiboList)
print(sum(evenfiboList))
