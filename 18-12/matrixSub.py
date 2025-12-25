rows = int(input(("Enter no.of rows: ")))
cols = int(input("Enter no.of cols: "))
matrix1 = []

print("Enter matrix elements row wise")

for i in range(rows):
    row=list(map(int,input().split()))
    matrix1.append(row)

matrix2 = []
print("Enter matrix elements row wise")
for i in range(rows):
    row = list(map(int,input().split()))
    matrix2.append(row)

result = []
for i in range(rows):
    row = []
    for j in range(cols):
        row.append(matrix1[i][j] - matrix2[i][j])
    result.append(row)

print("Result of two matrixes:")
for row in result:
    print(row)
    

