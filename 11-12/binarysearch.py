arr = list(map(int,input("enter the elements of array").split()))
#arr = [1,4,7,9,2,6,8]
x = int(input("enter the element to search"))
#x = 9
low = 0
high = len(arr)-1
found = False
while low <= high :
    mid = (low + high)//2
    if arr[mid] == x:
        print("Elements found at index:", mid)
        found = True
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1

if not found:
    print("element not found")
