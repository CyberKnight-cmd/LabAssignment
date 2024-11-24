exp = int(input("Enter the power : "))
base = int(input("Enter the base number : "))
result = 1
for i in range(exp):
    result*=base
print(result)