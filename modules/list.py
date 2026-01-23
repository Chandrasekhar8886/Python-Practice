#language = 'python'
#lst = set(language)
#print(type(lst))
#print(lst)

#lst = [i for i in language]
#print(type(lst))
#print(lst)

#num = [(i,i*i) for i in range(10) ]
#print(num)

#even = [i for i in range(10) if i % 2 == 0]
#print(even)

#list_of_lists = [[1,2,3], [4,5,6], [7,8,9]]
#flat_list = [number for row in list_of_lists for number in row]
#print(flat_list)

#num = lambda a,b :a-b
#print(num(25,15))

#multi_var = lambda a,b,c:a**2 - 3*b+4*c
#print(multi_var(5,5,3))

#def power(x):
#    return lambda n:x**n
#cube = power(2)(3)   # function power now need 2 arguments to run, in separate rounded brackets
#print(cube)
#two_power_of_five = power(2)(5) 
#print(two_power_of_five) 

#numbers = [-4, -3, -2, -1, 0, 2, 4, 6]
#def positive(numbers):
#    return list(filter(lambda x : x >= 0, numbers))
#print(positive(numbers))

#list_of_lists =[[1, 2, 3], [4, 5, 6], [7, 8, 9]]
#flat = [ x for sublist in list_of_lists for x in sublist]
#print(flat)


#lst = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10]
#result = [(n, *[n**i for i in range(6)]) for n in range(11)]
#print(result)

#countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#flat = [[c.upper(),c[:3],c.upper()] for [(c,cap)] in countries ]

#countries = [[('Finland', 'Helsinki')], [('Sweden', 'Stockholm')], [('Norway', 'Oslo')]]
#flat = [{'country': c.upper(), 'capital': cap.upper()} for [(c, cap)] in countries]
#print(flat)

#names = [[('Asabeneh', 'Yetayeh')], [('David', 'Smith')], [('Donald', 'Trump')], [('Bill', 'Gates')]]
#flat = [c + ' ' +cap for[(c,cap)] in names]
#print(flat)

def slope(x1,x2,y1,y2):
    return lambda x1,x2,y1,y2:(y2-y1)/(x2-x1) 
print(slope(7,6,5,4))


