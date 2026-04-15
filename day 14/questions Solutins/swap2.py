# Given two numbers, write a program to swap their values without using a third variable.

a=6
b=9

print("Before swapping: a =", a, "b =", b)
a = a+b # a now becomes 15
b = a-b # b now becomes 6
a = a-b # a now becomes 9

print("After swapping: a =", a, "b =", b)