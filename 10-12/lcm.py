import math

a=int(input("enter a number:"))
b=int(input("enter a number:"))

lcm = (a*b)// math.gcd(a, b)
print("LCM of ", a, "and", b,"is:", lcm)

#greater = max(a,b)
# if greater % a == 0 and greater % b == 0:
#     print(lcm == greater)
#    break
#greater +=1
#  