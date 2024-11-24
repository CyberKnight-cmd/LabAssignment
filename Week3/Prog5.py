def fact(a):
    if a<2:
        return 1
    else:
        return a*fact(a-1)
    
print(",".join([str(fact(i)) for i in range(1,int(input("Enter N = ")) + 1)]))