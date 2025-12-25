def is_sorted(arr):
    for i in range(len(arr)-1):
        if arr[i]>arr[i+1]:
            return False
    return True

arr =[38,27,43,3,9,82,10]
print("Is array sorted?", is_sorted(arr))