s = input("enter a string:")
s_lower = s.lower()
if s_lower == s_lower[::-1]:
    print("The string is palindrome")
else:
    print("the string is not a palindrome")
