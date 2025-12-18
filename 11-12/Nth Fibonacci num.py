n = int(input("enter a number"))

a,b = 0,1
if n == 1:
    print("1st Fibonacci number is:",a)
elif n == 2:
    print("2nd Fibonacci number is:",b)
else:
    for i in range(3, n + 1):
        a,b = b, a+b
    print(f"{n}th Fibonacci number is:",b)