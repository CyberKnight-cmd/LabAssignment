N = int(input("Enter N = "))
series = [str(i**2) for i in range(1,N+1)]
print(",".join(series))