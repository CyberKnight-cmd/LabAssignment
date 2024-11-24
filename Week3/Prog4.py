"""
1 + 1 = 2
2 + 2 = 4
4 + 4 = 8
8 + 8 = 16
16 + 7 = 23
23 + 5 = 28
"""

def sumOfDigits(num:int):
    return sum([int(digit) for digit in list(str(num))])

N,s = int(input("Enter N = ")), 1
for i in range(1,N+1):
    print(s,end=',')
    s+=sumOfDigits(s)
