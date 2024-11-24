"""
1 + 2 = 3
3 + 4 = 7
7 + 6 = 13
13 + 8 = 21
21 + 10 = 31
"""

N = int(input("Enter N = "))
series = [str(sum([(2*i) for i in range(1,j+1)]) + 1) for j in range(N)]
print(",".join(series))


"""
Actual logic : 

for i in range(N):
    sum = 1
    for j in range(1,i+1):
        sum+=2*j
    print(sum)
"""