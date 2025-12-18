arr = list(map(int,input("enter elements array:").split()))

largest = arr[0]
for num in arr:
    if num > largest:
        largest = num
print("Largest Number: ", largest)
