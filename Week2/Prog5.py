num = int(input("Enter a number : "))
factors = [1,num]
for i in range(2,num//2):
    if num%i==0 and i not in factors:
        factors+=[i,num//i]
print(sorted(factors))
# print(factors)
