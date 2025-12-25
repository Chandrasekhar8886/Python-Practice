def find_mean(arr):
    total = 0
    for num in arr:
        total += num
    mean = total / len(arr)
    return mean

arr = [10, 20, 30, 40, 50]
print("Mean of the array:", find_mean(arr))