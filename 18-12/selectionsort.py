arr = [6,5,9,3,2,4,8]
n = len(arr)  #7
for i in range(n - 1):  #6
    min_index = i   #0
    for j in range(i + 1,n):  #1,6
        if arr[j] < arr[min_index]:  #arr[j]<arr[min_index] = arr[1]<arr[0]
            min_index = j
    arr [ i] , arr[min_index ] = arr[min_index],arr[i]

print("Sorted array:", arr)

#Selection sort repeatedly selects
# the smallest element from the unsorted part and 
# places it at the beginning.