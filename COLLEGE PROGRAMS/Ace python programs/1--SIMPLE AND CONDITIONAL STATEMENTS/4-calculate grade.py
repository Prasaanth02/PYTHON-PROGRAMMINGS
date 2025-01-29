mark=int(input("ENTER YOUR MARK:"))
if mark >85 and mark<=100:
    print("CONGRATS!YOU SCORED GRADE A.....")
elif mark>60 and mark<=85:
    print("YOU SCORED GRADE B+...")
elif mark>40 and mark<=60:
    print("YOU SCORED GRADE B....")
elif mark>30 and mark<=40:
    print("YOU SCORED GRADE C...")
else:
    print("SORRY YOU ARE FAIL...!")