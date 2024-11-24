n = int(input("Enter nth term : "))
sequence = [2*3**(i-1) for i in range(1,n+1)]
print(",".join(sequence))