# WAP to print multiplication table of a number entered by user

num=int(input("Enter a number: "))

for i in range(1,11,1):
    print(num, "x", i, "=", num*i)

i=1
while i<=10:
    print(num, "x", i, "=", num*i)
    i+=1