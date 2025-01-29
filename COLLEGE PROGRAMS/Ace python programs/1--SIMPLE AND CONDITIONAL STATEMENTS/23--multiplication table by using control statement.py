num=int(input("Enter the number do you want to multipy:"))
limit=int(input("Enter the limit number:"))
while 1:
    i=1
    while i<=limit:
        print("%d x %d=%d" %(num,i,num*i))
        i=i+1
    choice =int(input("Do you want to continue the multiplication table?.. press 0 for no:"))
    if choice==0:
        break
    else:
        num=num+1