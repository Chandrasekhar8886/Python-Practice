arr =  list(map(int,input("Enter the elements in array").split()))
total = 0
n = len(arr)
for num in arr:
    total += num

avg = (total)/n
print("Average of elements in array is:",avg)

#print("sum of element of array is:" ,sum(arr)