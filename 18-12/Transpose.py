rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

matrix = []
print("Enter matrix elements row-wise:")

for i in range(rows):
    row = list(map(int, input().split()))
    matrix.append(row)

transpose = []

for j in range(cols):
    row = []
    for i in range(rows):
        row.append(matrix[i][j])
    transpose.append(row)

print("\nTranspose of matrix:")
for row in transpose:
    print(row)
