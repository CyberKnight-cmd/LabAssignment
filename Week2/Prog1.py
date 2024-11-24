day = ["Sunday","Monday", "Tuesday", "Wednesday","Thursday", "Friday","Saturday"]
num = int(input("Enter a number between 1 to 7: "))
print(day[num] if 0<num<8 else "Number Not In Range.")