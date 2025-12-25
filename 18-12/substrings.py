s = input("Enter a String")
n = len(s)
substrings = []
for i in range(n):
    for j in range(i + 1, n + 1):
        substrings.append(s[i:j])

print("All possible substrings are:")
print(substrings)