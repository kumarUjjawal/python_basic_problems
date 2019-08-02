def reverse(s):
    return s[::-1]

def is_palindrome(s):
    rev = reverse(s)

    if (s == rev):
        return True
    return False

s = "malayalam"
ans = is_palindrome(s)

if (ans == 1):
    print("yes")
else:
    print("No")

# Using built-in reverse function
def isPalindrome(s):
    # reverse to string print(s)
    rev = ''.join(reversed(s))

    # Checking if both string are equal or not
    if (s == rev):
        return True
    return False

s = "malayalam"
ans = isPalindrome(s)

if (ans == 1):
    print("Yes")
else:
    print("No")
