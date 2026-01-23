num = int(input("enter a number:"))
for i in range(1,num+1):
    digits = len(str(num))
    temp = num
    sum = 0
    while temp > 0:
        digit = temp%10
        sum += digit**digits
        temp //= 10
    if sum == num:
        print(num, end="")
