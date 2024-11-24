def fact(a):
    if a<2:
        return 1
    else:
        return a*fact(a-1)

s = 0
for i in range(1,8):
    s += i/fact(i)