arr = list(map(int,input("enter the elements of array").split()))

rev_arr = []
for i in range(len(arr)-1, -1, -1):
    rev_arr.append(arr[i])
    
print("Reversed array:",rev_arr)