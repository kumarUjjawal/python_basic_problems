# Find if the number is even or odd

def even_odd(num):
    if (num % 2) == 0:
        print("{0} is even.".format(num))
    else:
        print("{0} is odd".format(num))

num = 403
even_odd(num)
