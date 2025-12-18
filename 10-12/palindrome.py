num = int(input("enter a number"))
temp = num 
rev = 0
while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp = temp // 10

if num == rev:
    print(num," is palindrome")
else :
    print(num,"is not plaindrome")

#if num == num[::-1]:
#palindrome