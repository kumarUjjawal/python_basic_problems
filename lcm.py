# find the lcm of two numbers
def lcm(x,y):
    if x > y:
        greater = x
    else:
        greater = y
    while True:
        if((greater % x == 0) and (greater % y == 0)):
            lcm = greater
            break
        greater += 1
    return lcm

num1,num2 = 54,24
print(lcm(num1,num2))
