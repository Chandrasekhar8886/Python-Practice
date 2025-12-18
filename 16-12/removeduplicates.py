arr = [1,2,3,4,4,2,3,3]
unq_arr = [ ]
for num in arr:
    if num not in unq_arr:
        unq_arr.append(num)
print(unq_arr)

#unq_arr = list(set(arr))

 