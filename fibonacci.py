# Find the fibonacci series

n_terms = 10

n1 = 0
n2 = 1
count = 0

if n_terms < 0:
    print("Not a positive number")
elif n_terms == 0:
    print("Fibonacci series is",n1)
else:
    while count < n_terms:
        print(n1)
        nth = n1 + n2
        n1 = n2
        n2 = nth
        count += 1
