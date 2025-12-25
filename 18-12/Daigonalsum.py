n = int(input("Enter matrix size:"))
matrix = []

for i in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)

diag_sum = 0
for i in range(n):
    diag_sum += matrix[i][i]

print("Sum of daiagonal elements:",diag_sum)