num = str(int(input("Enter a number : ")))
print(num, "is a Palindrome number" if num==num[::-1] else "is not a Palindrome number")