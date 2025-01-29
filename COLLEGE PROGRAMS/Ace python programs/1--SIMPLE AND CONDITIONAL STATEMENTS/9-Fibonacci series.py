n=int(input("Enter a number:"))
n1,n2=0,1
count=0
if n<0:
    print("Please Enter terms is valid")
elif n==1:
    print("Fibonacci series")
    print(n1)
else:
    print("fibonacci series")
while count<n:
    print(n1)
    n3=n1+n2
    n1=n2
    n2=n3
    count+=1
    