#def gen_full_name(firstname,secondname):
    #return firstname+' '+secondname
#print(gen_full_name("chandu","reddy"))

#main.py file
#import random
#import string

#def random_user_id():
#    try:
#        len = int(input("enter no.of chars"))
#        count = int(input("enter no.of ids"))
#    except:
#        print("enter positive integers")
#    if len <= 0 or count <= 0 :
#        raise ValueError("enter positive integers")
#    chars = string.ascii_letters + string.digits
 #   ids = []
 #   for  _ in range(count):
 #       user_id = " "
 #       for _ in range(len):
 #           user_id += random.choice(chars)
 #       ids.append(user_id)
 #   return ids
#print(random_user_id())

#import random
#import string 
#def rgb_color_gen():
#    r = random.randint(0, 255)
#    g = random.randint(0, 255)
#    b = random.randint(0, 255)
#    return (r,g,b)
#print(rgb_color_gen())

#import random
#def list_of_hexa_colors(n):
#    hex_chars = "0123456789ABCDEF"
#    colors = []
#    for _ in range(n):
#        color = "#"
#        for _ in range(6):
#            color += random.choice(hex_chars)
#        colors.append(color)
#    return colors 
#print(list_of_hexa_colors(3))

