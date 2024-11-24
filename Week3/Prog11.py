a,b = map(int,input("Emter 2 numbers : ").split())
if b>a:
    a,b=b,a
for i in range(b,1,-1):
    if a%i==0 and b%i==0:
        print(f"HCF = {i}")
        break