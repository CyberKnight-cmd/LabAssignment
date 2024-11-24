num = int(input("Enter a number : "))
multiplicationTable = [f"{num} X {i} = {num*i}" for i in range(1,11)]
print("\n".join(multiplicationTable))