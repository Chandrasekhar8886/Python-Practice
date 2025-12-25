s = input("Enter a string:")
seen = set()
for ch in s:
    if ch in seen:
        print("First repeating character:", ch)
        break
    else:
        seen.add(ch)
else:
    print("No repeating characters found.")
