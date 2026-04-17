# WAP to reverse a number and check palindrome or not.


"""
121 -> 121
"""

"""
num = 1234 -> 4321
"""

num = int(input("Enter a number: "))
og = num
reverse = 0

while num >0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num = num // 10

if reverse == og:
    print("Palindrome")
else:
    print("Not Palindrome")