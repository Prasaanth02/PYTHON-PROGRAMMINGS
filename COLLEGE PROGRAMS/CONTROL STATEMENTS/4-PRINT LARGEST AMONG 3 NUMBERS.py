a=int(input("ENTER FIRST NUMBER:"))
b=int(input("ENTER SECOND NUMBER:"))
c=int(input("ENTER THIRD NUMBER:"))
if a>b and a>c:
    print("LARGEST NUMBER IS",a)
elif b>a and b>c:
    print("LARGEST NUMBER IS",b)
else:
    print("LARGEST NUMBER IS",c)