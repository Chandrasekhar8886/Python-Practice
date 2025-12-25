def to_binary(n):
    if n > 1:
        to_binary(n//2)
    print(n % 2, end=" ")

n = int(input("Enter a number :"))
print(to_binary(n))
#to_binary(15)
#The function recursively divides the number by 2 until it reaches 1,
# then prints the remainders while returning, 
# producing the binary representation in correct order.