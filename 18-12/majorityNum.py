def find_majority(arr):
    freq = {}
    for num in arr:
        freq[num] = freq.get(num,0) + 1
        if freq[num] > n//2:
            return  num
    return -1

arr = [3,3,4,2,4,4,2,4,4]
n = len(arr)
print("Majority element is:", find_majority(arr))