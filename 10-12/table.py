num = int(input("enter a number:"))
limit = int(input("Enter limit:"))
print("Multiplication table of", num, "is:")

for i in range(1,limit + 1):
    print(f"{num} x {i} = {num * i}")