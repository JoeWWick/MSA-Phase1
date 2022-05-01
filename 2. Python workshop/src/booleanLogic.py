a = 16
b = 25
c = 27
if a > b:
    if b > c:
        print ("a is greater than b and b is greater than c")
    else: 
        print ("a is greater than b and less than c")
elif a == b:
    print ("a is equal to b")
else:
    print ("a is less than b")


a = 23
b = 34
if a == 34 or b == 34:
    print(a + b)

a = 23
b = 34
if a == 34 and b == 34:
    print (a + b)