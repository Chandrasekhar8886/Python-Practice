
arr = list(map(int,input("enter elements of array:").split()))
n =len(arr)
k = int(input("Enter element to search:"))
found = False
for i in  range(n):
    if arr[i] == k:
        print("Element found at indx:",i)
        found = True
        break
if not found:
    print("Element not found")