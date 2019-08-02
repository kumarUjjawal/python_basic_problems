# Find the factorial of a number with recursion

def rec_factorial(num):
    if num == 1:
        return num
    else:
        return num * rec_factorial(num - 1)

num = 7

if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of",num,"is",rec_factorial(num))
