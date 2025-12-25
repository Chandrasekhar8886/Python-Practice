s = input("Enter a String : ")
duplicates = " "
for ch in s:
    if ch not in duplicates:
        duplicates += ch
print(duplicates) 