rows = int(input("Enter no.of rows"))
columns = int(input("Enter no.of columns"))
for i in range(rows):
    for j in range(columns):
        if (i+j)%2 == 0:
            print("X", end=" ") 
        else:
            print("0", end="  ")
    print()