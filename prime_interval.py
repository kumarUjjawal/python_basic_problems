# find prime numbers in interval

def prime(lower,upper):
    for num in range(lower,upper + 1):
   # prime numbers are greater than 1
        if num > 1:
            for i in range(2,num):
                if (num % i) == 0:
                    break
            else:
                print(num)

lower = 900
upper = 1000

prime(lower,upper)
