#def find_even_numbers(n):
    #even = []
    #for i in range(n +1):
   #     if i % 2 == 0:
  #          even.append(i)
 #   return even


#print(find_even_numbers(10))
#def area_of_circle(r):
#    area = 3.14*r*r
#    return area
#print(area_of_circle(3))

#def convert_celsius_to_fahrenhiet(c):
#    f = (c*9/5) + 32
#    return f
#print(convert_celsius_to_fahrenhiet(37))

#def check_slope(x1,x2,y1,y2):
#    slope = (y2-y1)/(x2-x1)
#    return slope
#print(check_slope(1,2,3,4))

#def quadratic_equation(a,b,c):
#    d = (b**2)-(4*a*c)
#    sol1 = (-b + d**0.5)/(2*a)   
#    return sol1
#    sol2 = (-b -d**0.5)/(2*a)
#    return sol2
#print(quadratic_equation(1,-3,2))

#def print_list(lst):
#    if not isinstance(lst, list):
#        raise TypeError("Input must be a list")
#
#    for item in lst:
#        print(item)
#print(print_list(lst=[1, 2, 3, 4, 5]))

#def reverse_list(lst):
#    reversed_list = []
#    for i in range(len(lst)-1,-1,-1):
#        reversed_list.append(lst[i])
#    return  reversed_list 
#print(reverse_list(lst=[1, 2, 3, 4, 5]))

def capitalize_list_items(lst):
    
    for i in range(len(lst)):
        lst[i] = lst[i].upper()
        return lst
print(capitalize_list_items(['sdfvdf','banana','camle']))