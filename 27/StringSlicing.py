#string slicing
challenge = 'thirty days of python'
sub_string = 'da'
print(challenge.index(sub_string))  # 7
#print(challenge.index(sub_string, 9)) # error
#rindex(sub_string,9) search start from index 9
print(challenge.rindex(sub_string))  # 7
#print(challenge.rindex(sub_string,9)) # error
print(challenge.rindex('on', 8)) # 19
print(challenge.isalnum()) # space is not considered as alpha numeric

