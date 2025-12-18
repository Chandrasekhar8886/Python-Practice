p = int(input("enter principle amount"))
t = int(input("enter time"))
r = int(input("enter rate of intrest"))
A = p * (1 + r/100) ** t
CI = A - p
print("Compound Interest:",CI)
print("Total Amount:",A)