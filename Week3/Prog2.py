N = int(input("Enter N = "))
series = [str(2**i) for i in range(1,N+1)]
print(",".join(series))