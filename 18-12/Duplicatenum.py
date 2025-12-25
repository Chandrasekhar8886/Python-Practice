def find_duplicate(arr):
    freq = {}
    for num in arr:
        if num in freq:
            return num
        freq[num] = 1

arr = [1,2,3,4,5,3]         
print("Duplicate number is:",find_duplicate(arr))