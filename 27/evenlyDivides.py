def evenlyDivides(n):
    count = 0
    for digit in str(n):
        digit = int(digit)
        if digit != 0 and digit % n == 0:
            count+= 1
    return count

n = 120
print(evenlyDivides(n))  