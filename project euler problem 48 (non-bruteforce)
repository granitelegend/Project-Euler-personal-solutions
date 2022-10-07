# Project Euler Problem 48

# The idea is to produce the sum as a number and then convert and interate the number to a string from the end to start.
# This will produce a reverse list of digits, which is then reversed to produce the preferred order of digits.

sumSeries = 0
a = 0
digitList = []

for x in range(1, 1001):  # Sum of series
    sumSeries = x ** x + sumSeries

strSum = str(sumSeries)  # Converting sum to string
a = len(strSum) - 1

while a != len(strSum) - 11:  # Stop when having iterated 10 digits
    digitList.append(strSum[a])  # Creating the list of the last 10 digits in incorrect order
    a -= 1

digitList.reverse()  # Correction of the order of the last 10 digits.
print(digitList)
