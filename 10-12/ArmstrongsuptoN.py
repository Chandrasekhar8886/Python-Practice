n = int(input("enter a number"))
print("Armstrong numbers b/w 1 and", N,"are:")
for num in range(1,N+1):
    digits = str(num)
    n = len(digits)

    sum_power = 0
    for d in digits:
       sum_power += int(d) ** n
    if sum_power == num:
        print(num,end=" ")