def find_min(arr,n):
    if n == 1:
        return arr[0]
    return min(arr[n -1],find_min(arr,n - 1))

arr = list(map(int,input("Enter elements of array:").split()))
print("Min element :", find_min(arr,len(arr)))