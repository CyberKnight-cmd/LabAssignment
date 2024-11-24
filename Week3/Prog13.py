n = int(input("Enter n = "))
s = 1
for i in range(2,n+1):
    s+=1/i if i%2==0 else -1/i
print(s)