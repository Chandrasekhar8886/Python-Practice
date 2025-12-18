num = int(input("enter a num"))
digits = str(num)
n = len(digits)

sum_power = sum(int(d)**n for d in digits)

if sum_power == num:
    print(num,"is a Armstrong number")
else:
    print(num,"is not an armstrong number")