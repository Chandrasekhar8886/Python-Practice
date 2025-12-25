s = input("Enter a string:")
vowels = "AEIOUaeiou"
result = " "
for ch in s:
    if ch not in vowels:
        result += ch

print(result)

