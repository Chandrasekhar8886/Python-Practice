arr = [5, 2, 9, 1, 6, 3]

smallest = second_smallest = float('inf')  
for num in arr:
    if num < smallest:
        second_smallest = smallest
        smallest = num
    elif num < second_smallest and num != smallest:
        second_smallest = num

print("Second smallest element:", second_smallest)


#arr.sort()
#print(arr[-2])