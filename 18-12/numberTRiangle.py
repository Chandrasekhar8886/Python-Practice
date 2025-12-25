n = int(input("Enter no.of rows"))
for i in range(n):
    print(" "*(n-1), end=" ")
    for j in range(1,i+1):
        print(j, end=" ")
    print()
    