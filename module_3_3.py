#1
def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params()
print_params( 7, None, False)
print_params(b=25)
print_params(c = [1,2,3])
#2
values_list = ['Красота', 76, False]
values_dict = {'a': 256.2547, 'b': 'Director', 'c': False}
print_params(*values_list)
print_params(**values_dict)
#3
values_list_2 = ['Raven', 88]
print_params(*values_list_2, 42)
