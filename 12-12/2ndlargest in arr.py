
arr = list(map(int,input("enter the elements of array").split()))

largest = second_largest = float('-inf')

for num in arr:
    if num > largest :
        second_largest = largest
        largest = num
    elif num > second_largest and num != largest:
        second_largest = num

print("Second Largest Element:",second_largest)

#arr.sort()
#print(arr[-2])