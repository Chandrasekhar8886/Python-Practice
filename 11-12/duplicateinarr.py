arr = list(map(int,input("enter the elements of array").split()))

duplicates = set()
seen = set()

for num in arr:
    if num in  seen:
        duplicates.add(num)
    else:
        seen.add(num)
print("Duplicate elements:", list(duplicates))
