digits = list(str(int(input("Enter the number:"))))
print("Armstrong Number!!" if int("".join(digits))==sum([int(i)**len(digits) for i in digits]) else "Not an Armstrong number")