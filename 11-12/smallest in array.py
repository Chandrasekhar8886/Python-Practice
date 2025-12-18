arr = list(map(int,input("enter elements array:").split()))

smallest = arr[0]
for num in arr:
    if num < smallest:
        smalllest = num
print("smallest Number: ", smallest)
