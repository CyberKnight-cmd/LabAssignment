count = [0,0,0]

numbers = sorted(list(map(int,input("Enter all the numbers : ").split())))

for number in numbers:
    if number<0:
        count[0]+=1
    elif number==0:
        count[1]+=1
    else:
        count[2]+=1

print(f"Entered numbers : {",".join([str(number) for number in numbers])}\nNumber of positives : {count[2]}\nNumber of zeroes : {count[1]}\nNumber of negatives : {count[0]}")