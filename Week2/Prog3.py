def fact(a:int) -> int :
    if a<2:
        return 1
    else:
        return a*fact(a-1)
    
print(fact(int(input("Enter the number : "))))