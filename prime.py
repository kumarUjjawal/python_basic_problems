# Find if the numer is prime or not
def prime(num):
    if (num > 1):
        for i in range(2,num):
            if (num % i) == 0:
                print("Not Prime")
                break
        else:
            print("Prime")
    else:
        print("Not Prime")

num = -1
prime(num)
