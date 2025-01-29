def function(*args):
    num=0
    for arg in args:
        num=num+arg
    return num
    print(num+arg)
print(function(100,30))
print(function(100,30,20))
