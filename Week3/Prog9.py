enteredNumbers = []
pointer = 1
while(pointer>0):
    n = int(input("Enter a number : "))
    if n==0:
        pointer-=1
    else:
        enteredNumbers.append(n)

avg = sum(enteredNumbers)/len(enteredNumbers)
print(avg)