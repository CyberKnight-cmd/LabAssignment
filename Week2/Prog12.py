# WAP to find sum  of squares of first n natural number.
N = int(input("Enter N = "))
squares = [num**2 for num in range(1,N+1)]
print(f"{sum(squares)} is the sum of first {N} natural numbers")