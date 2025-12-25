def find_missing(arr,N):
    expected_sum = N * ( N + 1 ) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum

arr = [1,2,4,5,6]
N = 6   
print("Missing number is:",find_missing(arr,N))