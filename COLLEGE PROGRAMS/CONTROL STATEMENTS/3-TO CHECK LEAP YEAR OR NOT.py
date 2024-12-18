year=int(input("ENTER THE YEAR:"))
if(year%400==0) and (year%100==0):
    print(year,"IS A LEAP YEAR")
elif(year%4==0) and (year%100!=0):
    print(year,"IS A LEAP YEAR")
else:
    print(year,"IS NOT A LEAP YEAR")