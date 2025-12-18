arr  = list(map(int,input("enter the elements of arr").split()))
#k = input("enter k: ")
k = 2

k = k % len(arr)  
#k = k % len(arr)
rotated = arr[-k:] + arr[:-k]
print("Array after rotation:", rotated) 