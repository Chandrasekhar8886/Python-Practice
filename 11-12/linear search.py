arr = list(map(int,input("enter the elements of array").split()))
#arr = [1,4,7,9,2,6,8]
x = int(input("enter the element to search"))
#x = 9
found = False
for i in range(len(arr)):
    if arr[i] == x:
        print("Element found at index:",i)
        found = True
        break

if not found :
    print("Element not found")
