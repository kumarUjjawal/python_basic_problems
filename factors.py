# Find factors of a number

def factors(num):
    for i in range(1, num+1):
        if num % i == 0:
            print(i)

num = 320
factors(num)
