arr = list(map(int,input("enter the elements of array").split()))
n = len(arr)

for i in range(n):
    for j in range(0,n - i - 1):
        if arr[j] < arr[j+1] :
            arr[j],arr[j+1] = arr[j+1],arr[j]

print("Array in descending order:",arr)

#arr.sort(reverse=True)
#desc_arr = sorted(arr,reverse=Ture)