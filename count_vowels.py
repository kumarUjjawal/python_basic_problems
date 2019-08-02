# Count the number of vowels in a string

str = "Hello World"

str = str.casefold()

count = {x:sum(1 for char in str if char == x) for x in 'aeiou'}
print(count)
