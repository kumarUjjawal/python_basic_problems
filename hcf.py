# find the hcf of two numbers
def compute_hcf(x,y):
    if x > y:
        smaller = y
    else:
        smaller = x
    for i in range(1,smaller + 1):
        if ((x % i == 0) and (y % i == 0)):
            hcf = i
    return hcf

num1,num2 = 54,24
print(compute_hcf(num1,num2))

# Euclidean Algorithm
def comp_hcf(x,y):
    while (y):
        x,y = y, x%y
    return x
num1,num2 = 54,24
print(comp_hcf(num1,num2))
