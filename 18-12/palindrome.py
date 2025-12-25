def is_palin(s,start,end):
    if start >= end:
        return True
    if s[start] != s[end]:
        return False
    return is_palin(s,start + 1,end-1)

string = input("enter a string :")
if is_palin(string,0,len(string)-1):
    print("palindrome")
else:
    print("not a palindrome")




