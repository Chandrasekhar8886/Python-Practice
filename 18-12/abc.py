rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

print("Enter matrix elements row-wise:")    
matrix1 = []
for i in range(rows):
    row = list(map(int,input().split()))
    matrix1.append(row)

print("enter elements for second matrix:")
matrix2 = []
for i in range(rows):
    row  = list(map(int,input().split()))
    matrix2.append(row)

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] + matrix2[i][j])
    result.append(row)

print("\n Sum of matrices:")
for row in result:
    print(row)