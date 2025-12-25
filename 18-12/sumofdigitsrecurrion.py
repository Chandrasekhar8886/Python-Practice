def sum_of_digits(n):
    if n == 0:
        return 0
    return n % 10 + sum_of_digits(n//10)

num = int(input("Enter  a number:")) 
result = sum_of_digits(abs(num))
print("Sum of digits:", result)