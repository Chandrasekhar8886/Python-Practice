def binary_to_decimal(b,i =0):
    if  b == 0:
        return 0
    return(b % 10) * (2**i) +binary_to_decimal(b // 10,i + 1)
Binary = int(input("Enter a binary number:"))
print("Decimal:",binary_to_decimal(Binary))
