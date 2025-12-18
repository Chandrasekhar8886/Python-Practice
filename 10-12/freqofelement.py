arr = [1,2,3,4,4,2,3,3]
freq = {}
for num in arr :
    if num in freq:
        freq[num] += 1
    else :
        freq[num] = 1
print(freq)
