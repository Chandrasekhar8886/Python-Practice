def find_median(arr):
    n = len(arr)
    arr.sort()

    if n % 2 == 1:
        return arr[n//2]
    else :
        mid1 = arr[n//2 - 1]
        mid2 = arr[n//2]
        return(mid1 + mid2) / 2
    
arr = [38,5,1,53,87,55,92,4]
print("Median is:",find_median(arr))