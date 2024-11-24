def fact(a:int):
    if a<2:
        return 1
    else:
        return a*fact(a-1)

digits = list(str(int(input("Enter a number : "))))
processed = sum([fact(int(digit)) for digit in digits])
print(f"{"".join(digits)} is a Krishnamurthy number!" if int("".join(digits))==processed else f"{"".join(digits)} is not a Krishnamurthy number!" )