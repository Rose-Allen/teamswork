'''Задача 1
def square(x):
    return x * x




def print_hello():
    print("Привет, мир!")
'''











''' Задача 2
def create():
    my_list = [1, 2, 3, 4, 5]
    my_tuple = ("Javascript", "React", "ReactNative")
    my_dict = {"name": "Dinur", "age": 21, "city": "Almaty"}
    return my_list, my_tuple, my_dict   


my_data = create()

my_list = my_data[0]
my_tuple = my_data[1]
my_dict = my_data[2]

print(my_list)  
print(my_tuple)
print(my_dict)
'''







'''Задача 3
numbers = [1, 2, 3, 4, 5]
x2chisla = list(map(lambda x: x * 2, numbers))
print(x2chisla)

numbers = [1, 2, 3, 4, 5]
chetnye = list(filter(lambda x: x % 2 == 0, numbers))
print(chetnye)

from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum = reduce(lambda x, y: x + y, numbers)
print(sum)
'''




'''Задача 4
def calculate(street, tovar):
    dostavka = 0
    if street in ["Аль-Фараби", "Саина", "Ташкентская", "Достык"]:
        if tovar < 10000:
            dostavka = 500
    else:
        if tovar < 10000:
            dostavka = 1000
        else:
            dostavka = 0
    return dostavka

street = "Аль-Фараби"
tovar = 8000
total = calculate(street, tovar)
print(f"Total delivery cost: {total} KZT")
'''







'''Задача 5
def compose(f, g):
    def h(x):
        return f(g(x))
    return h

def f(x):
    return x ** 2

def g(x):
    return x + 2

h = compose(f, g)
result = h(3)

print(result)
'''