# find fibonacci series with recursion

def recur_fibonacce(num):
    if num <= 1:
        return num
    else:
        return recur_fibonacce(num - 1) + recur_fibonacce(num - 2)

n_terms = 10
if n_terms < 0:
    print("Not a positive number")
else:
    for i in range(n_terms):
        print(recur_fibonacce(i))
