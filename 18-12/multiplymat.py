rows1 = int(input("enter no.of rows for mat1:"))
cols1 = int(input("enter no.of cols for mat1:"))

rows2 = int(input("enter no.of rows for mat2:"))        
cols2 = int(input("enter no.of cols for mat2:"))
if cols1 != rows2:
    print("Multiplication is not possible!")
    exit()

print("Enter matrix1 elements row-wise:")
mat1 = [list(map(int,input().split())) for _ in range(rows1)]

print("Enter elements of mat2:")
mat2 = [list(map(int,input().split())) for _ in range(rows2)]

result = [[0 for _ in range(cols2)] for _ in range(rows1)]

for i in range(rows1):
    for j in range(cols2):
        for k in range(cols1):
            result[i][j] += mat1[i][k] * mat2[k][j]

print("\n Product of mat:")
for row in result:
    print(row)