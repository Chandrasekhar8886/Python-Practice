def find_mode(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0) + 1 

    max_count =  max(freq.values())
    mode = []
    for key,values in freq.items():
        if values == max_count:
            mode.append(key)
    return mode

arr = [1,2,2,3,4,4,4,5,5]
print("Mode of the array is:", find_mode(arr))


