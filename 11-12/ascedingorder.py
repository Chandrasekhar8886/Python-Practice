arr = list(map(int,input("enter elemngts of array").split()))
n = len (arr)
for i in range(n):
    for j in range(0,n-i-1):
        if arr[j] > arr[j+1]:
            arr[j],arr[j+1] = arr[j+1],arr[j]

print("Array in ascending order: ",arr)

#sorted_arr = sorted(arr)
#arr.sort()