def evenlyDivides(n):
    count = 0
    temp = n
    while temp > 0:
        digit = temp % 10 
        if digit != 0 and digit % n == 0:
            count+= 1
    return count

n = 120
print(evenlyDivides(n))  