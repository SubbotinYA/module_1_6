#Создайте переменную  и присвойте ей словарь из нескольких пар ключ-значение.
my_dict={'dink': 'juice', 'eat': 'barbecue', 'soup': 'borsch' }
#Выведите на экран словарь my_dict
print(my_dict)
#Выведите на экран одно значение по существующему ключу, одно по отсутствующему из словаря my_dict
print(my_dict['eat'])
#Добавьте ещё две произвольные пары того же формата в словарь my_dict
my_dict.update({'cake': 'cupcake',
                'salad': 'caesar'})
#Удалите одну из пар в словаре по существующему ключу из словаря my_dict и выведите значение из этой пары на экран
del my_dict['soup']
print(my_dict)

#Создайте переменную my_set и присвойте ей множество, состоящее из разных типов данных с повторяющимися значениями
my_set = {1, 2, 3, 8, 8, 1, 9, 3}
#Выведите на экран множество my_set (должны отобразиться только уникальные значения)
print(my_set)
#Добавьте 2 произвольных элемента в множество my_set, которых ещё нет.
my_set.add(11)
my_set.update([12, 12, 15, 16])
print(my_set)
#Удалите один любой элемент из множества my_set
my_set.remove(8)
my_set.discard(123)
#Выведите на экран измененное множество my_set
print(my_set)