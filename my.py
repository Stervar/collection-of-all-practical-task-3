# Модуль 1 (часть 2)

#1
#print("Введите три числа:")

#a = int(input())
#b = int(input())
#c = int(input())

#d = a + b + c

#print(a, "+", b, "+", c, "=", d)
#2

#print() 

#x = int(input('введите зарплата за месяц'))   
#y = int(input('введидь сумма месячного платежа по кредиту в банке'))    
#z = int(input('введидь задолженность за коммунальные услуги.'))

#summa_plat= x - y - z 

#print(x, "-", y, "-",  z,"=" , summa_plat)
  
# 3
# print("Найдите S")

# d1 = int(input("видите число"))
# d2 = int(input("видите другое число"))

# s = (d1+d2)/2 

# print('(',d1, "+", d2, ")/2=", s)

#4

# print("To be")
# print("or not")
# print("to be")

#5

# print("'Life is what happens \n    when\n       you’are busy making other plans\n                                  John Lennon.\n")

# Модуль 1 (часть 3)
 
#1

# a = int(input("Введите число №1"))

# v = int(input(("Введите число №2")))

# n = int(input(("Введите число №3")))

# print(a,v,n)


# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# print(a*100+b*10+c)

#2

# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# g = int(input("Введите число №4"))


# s = (a * b * c * g) 

# print("Площадь параллелепида равна" ,a, "*",b, "*",c,"*",g,"=",s)

# №3



# a = float(input("Введите количество метров"))

# s = (a * 100)
# print ("Сумма сантиметров в метрах  равна ", s, "сантиметров")

# a = float(input("Введите количество метров"))

# s = (a * 10)
# print ("Сумма сантиметров в метрах  равна ", s, "дацеметров")

# a = float(input("Введите количество метров"))

# s = (a * 1000)
# print ("Сумма сантиметров в метрах  равна ", s, "милимтров")

# a = float(input("Введите количество метров"))

# s = (a *  0.000621)
# print ("Сумма сантиметров в метрах  равна ", s, "миль")



#№4

# a = int(input("размер основания треугольника"))

# h = int(input("размер высоты треугольника"))

# summa_plat= S = (a*h)/2

# print("Площадь  треугольника равен ", S)

# print(a,"*"  , h, "/2 = ", S )

# №5
# (запарестый способ)

# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# g = int(input("Введите число №4"))

# v = print(a*1000+b*100+c*10+g)

# v = input("Повторите результат если хотите перевернуть число")

# v = v[::-1]

# print(v)


# (легкий способ)

# number = input()
# number = number[::-1]
# print(number)


#Модуль 2 Операторы ветвлений (Часть 1)

# №1
# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# operation = input("Выберете один из вариантов решения - (+,*):")

# if operation == "+":
#     print(a + b + c)

# elif operation == "*":
#     print(a * b * c)
# else:
#     print("Вы ввели неверный оператор")



# Почему так нельзя делать?
# y = print(a * b * c) 
  
# y = print("сумма трех чисел равна")


# if print ==  2:  

# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# y=summa_plat= S = a * b * c 
# y=print("сумма трех чисел равна")
# y=print(S)
    
# №2
 
    
# a = int(input("Введите число №1"))

# b = int(input("Введите число №2"))

# c = int(input("Введите число №3"))

# all = [a, b, c]

# operation = input("Выберете один из вариантов решения чтобы найти последовательность - (a,b,c):")

# if operation == "a":
#       print ('Максимум из 3:', max(all))
# elif operation == "b":
#     print ('Минимум из 3:', min(all))
# elif operation == "c":
#      print('Среднее из 3:', sum(all) / len(all))
# else:
#     print("Вы ввели неверный вариант")

# №3



# a = int(input("Введите количество метров"))

# operation = input("Выберете один из вариантов решения - (мили,дюймы,ярды): ")

# if operation == "мили":
#     print ('Мили:', a * 0.000621371192)

# if operation == "дюймы":
#     print ('Дюймы:', a * 39.3700787)

# if operation == "ярды":
#     print ('Ярды', a * 0.9144)
# else:
#     print("Вы ввели неверный вариант")



#Модуль 2 Операторы ветвлений (Часть 2)

# №1



# operation = input("Введите номер недели (1,2,3,4,5,6,7): ")
# if operation == "1":
#     print("Понедельник")
# if operation == "2":
#     print("Ввторник")
# if operation == "3":
#     print("Среда")
# if operation == "4":
#     print("Четверг")
# if operation == "5":
#     print("Пятница")
# if operation == "6":
#     print("Суббота")
# if operation == "7":
#     print("Восскресенье")
# else:
#     print("Вы ввели неверный вариант")

# №2

# num = int(input("Введите номер месяца (1,2,3,4,5,6,7,8,9,10,11,12): "))
# month = ['Январь','Февраль'///]
# print(month[num-1])
# if operation == "1":
#     print("Январь")
# if operation == "2":
#     print("Февраль")
# if operation == "3":
#     print("Март")
# if operation == "4":
#     print("Апрель")
# if operation == "5":
#     print("Май")
# if operation == "6":
#     print("Июнь")
# if operation == "7":
#     print("Июль")
# if operation == "8":
#     print("Август")
# if operation == "9":
#     print("Сентябрь")   
# if operation == "10":
#     print("Октябрь")
# if operation == "11":
#     print("Ноябрь")
# if operation == "12":
#     print("Декабрь")

#№3

# peration = input("Введите число")

# peration = int(peration)

# if peration < 0:
#     print("«Number is negative»,")
# if peration > 0:
#     print("«Number is positive»,")
# if peration  == 0:
#     print("«Number is equal to zero»")

#№4

# a = input("Введите число №1 :")

# p = input("Введите число №2 :")


# if a == p: print('Эти два числа равны')

# elif a != p: print('Эти два числа не равны')

# if a > p: print('Первое число больше второго')

# if a < p: print('Второе число больше первого')


#Модуль 2 Операторы ветвления (Часть 3)

#№1

# a = int(input("Введите число от 1-100"))

# if  1 <=  a <= 100: 
#     print("Число входит в диапазон от 1 до 100:")
    
# # if a != 1 or a != 100:
# #         print("Ошибка")

# elif not a %3 == 0 :
#     print("Fizz")

# elif not a % 5 == 0:
#     print("Buzz")

# if not a % 3 == 0 and not a % 5 == 0:
#     print("Fizz Buzz")
# else:
#     print(a)
# else :
#  print("Ошибка,введите число в диапазоне [1; 100]")
# почему сдесь не поучаеться вести вторую если..?

#№2
# b = int(input("Введите число от 1-100"))

# a = int(input("Введите в каую степень вы хотите возвести число[0-7]:"))

# if 0 <= a <= 7:
  
#   print(a ** b)

# else:

#     print("Ошибка,введите число в диапазоне [0; 7]")

#3

# a = int(input("Введите стоимость разговора:"))
# b = int(input("Выбирите одного из опреторов [1-2-3-4]:"))

# if b == 1:
#     print(a * 0.95)
#     print("стоимость тарифа в руб")
# if b == 2:
#     print(a * 0.92)
#     print("стоимость тарифа в руб")
# if b == 3:
#     print(a * 0.9) 
#     print("стоимость тарифа в руб")
# if b == 4:
#     print(a * 0.85) 
#     print("стоимость тарифа в руб")

#4 (x/100*10)

# r = int(input("Введите сумму продаж для 1 менеджера [ОТ 500-1000]:"))
# a = int(input("Введите уровень продаж  для 1 менеджера[ОТ 3-8%]:"))

# if print(r/100*a):
#     print("1 менеджер")


# n = int(input("Введите сумму продаж для 2 менеджера [ОТ 500-1000]:"))
# b = int(input("Введите уровень продаж  для 2 менеджера[ОТ 3-8%]:"))

# if print(n/100*b):
#  print("2 менеджер")


# m = int(input("Введите сумму продаж для 3 менеджера [ОТ 500-1000]:"))
# c = int(input("Введите уровень продаж  для 3 менеджера[ОТ 3-8%]:"))


# if  print(m/100*c):
#  print("3 менеджер")



# g = int(input("Какой мененджр лучше всех сделал свою работу?: "))

# if not g == 1:
#     print(r/100*a  + 200)
#     print("1 менеджер получает прибавку 200$")

# elif not g == 2:
#     print(n/100*b + 200)
#     print("2 менеджер получает прибавку 200$")

# elif not  g == 3:
#     print(r/100*a + 200)
#     print("3 менеджер получает прибавку 200$")

# else:
#     print("Такого менеджера нет")



#Модуль 3 Цикл: (Часть 1)

# №1

# a = int(input("Ведите число номер 1(начало):"))

# b = int(input("Ведите число номер 2(конец):"))


# for i in range(a, b):
#     print(i)
#     if i == a:
#         print("Начало")
# if i == b:
#         print("Конец")
#         for i in range(a,b+1): 
#  (i%7==0):
#  print(i)
# else a == b:
#         raise RuntimeError
# print('Числа не могут быть одинаковыми')

# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# for i in range(a, b +1):
#     print(i)
#     if i == a:
#         print("Начало")
#     if i == b:
#         print("Конец")
#     if i % 7 == 0:
#         print(f"Найдена кратная 7: {i}")

# №2

# a = int(input("Ведите число номер 1(начало): "))
# b = int(input("Ведите число номер 2(конец): "))

# for i in range(a-1, b-1,-1 ):
#     print(i)
#     if i == a:
#         print("начало:")
#     if i == b:
#         print("конец:")
        
#     if i % 7 == 0:
#         print(f" Найдена кратная 7: {i}")
#     if i % 5 == 0:
#         print(f"Найдена кратная 5: {i}")

# №3

# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# for i in range(a, b +1):
#     print(i)
#     if i == a:
#         print("Начало")
#     if i == b:
#         print("Конец")
#     if i % 3 == 0:
#         print(f"Fizz: {i}")
#     if i % 5 == 0:
#         print(f"Buzz: {i}")
#     if i % 3 and 5 == 0:
#         print(f"Fizz Buzz: {i}")
#     if not i % 3 and 5 == 0:
#         print(f"Cамо число{i}")


# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# for i in range(a, b +1):
#     print(i)
#     if i == a:
#         print("Начало")
#     if i == b:
#         print("Конец")
#     if i % 3 == 0:
#         print(f"Fizz: {i}")
#     if i % 5 == 0:
#         print(f"Buzz: {i}")
#     if i % 3 == 0 and i % 5 == 0:
#         print(f"Fizz Buzz: {i}")
#     if not i % 3 and not i % 5:
#         print(f" не делиться не на 3 не на 5{i}")

# №4


#Модуль 3 Цикл: (Часть 2)

# №1

# a = int(input("Ведите число номер 1(начало):"))
# b = int(input("Ведите число номер 2(конец):"))

# sred_arvmet = 0
# nine_sum = 0

# for i in range(a, b +1):

#     print(i)
#     if i == a:

#         print("Начало")
#     if i == b:

#         print("Конец")
#     if i % 9 == 0:

#         print(f"кратно:{i}")

#     if i % 2 == 0:
#      nine_sum = 0
#      sred_arvmet += 1
#      print(f"четное: {i}")   

#     else: not i % 2 == 0
#     nine_sum  += i
#     sred_arvmet += 1
#     print(f"нечётное: {i}")    

#     print(f"Среднеарифметическое нечетных чисел:{sred_arvmet/nine_sum }")
  
# №2

# length = int(input("Введите длину линии: "))
# symbol = input("Введите символ для заполнения линии: ")

# for i in range(length):
#     print(symbol)

# №3

# a = int(input("Ведите число больше [0]:"))
# if a < 0 :
#     print("«Number is positive»")
# if 0 > a: 
#     print("«Number is negative»")
# else:
#     print("Number is equal to zero")

# if a == 7:
#     print("Good bye!")
        

#№4
# a = int(input("Ведите число 1:"))
# b = int(input("Ведите число 2:"))
# c = int(input("Ведите число 3:"))
# 19

# if a > b and a > c:
#  print("Макимально число[A]:", a)

# elif b > a and b > c:
#  print("Макимально число[B]:", b)


# elif c > a and c > b:
#  print("Макимально число[С]:", c)

# Модуль 3 Циклы.(Часть 3)

# # №1
# x = int(input("Ведите чётное число [1]:"))

# y = int(input("Ведите чётное число [2]:"))

# результат = pow(x,y)

# print(результат)

# №2

# Подсчитать количество целых чисел в диапазоне от
# 100 до 999 у которых есть две одинаковые цифры.

# count = 0 
# for i in range(100, 1000): 
#     num = str(i) 
#     if num[0] == num[1] or num[0] == num[2] or num[1] == num[2]: 
#         count += 1 
# print(count)

# №3

# Подсчитать количество целых чисел в диапазоне от
# 100 до 9999 у которых все цифры разные.

# count = 0
# for i in range(100, 10000):
#     num = str(i)
#     if num[0] != num[1] and num[0] != num[2] and num[0] != num[
#         3] and num[1] != num[2] and num[1] != num[3] and num[2]
#         != num[3]:
#         count += 1
# print(count)

# №4

# Пользователь вводит любое целое число. Необхо-
# димо из этого целого числа удалить все цифры 3 и 6 и
# вывести обратно на экран.

# a = int(input("Ведите любое целое число:"))

# ???????

# Модуль 3 Циклы.(Часть 4)

# №1

# Показать на экран все простые числа в диапазоне,
# указанном пользователем. Число называется простым,
# если оно делится без остатка только на себя и на единицу.
# Например, три — это простое число, а четыре нет.

# a = int(input("Ведите число которое будет являться начлом диапозонна: "))

# b = int(input("Ведите число которое будет являться концом диапозонна: "))

# for i in range(a,b +1):

#     is_prime = True
    

#     for j in range(2, i):

#         if i % j == 0:

#             is_prime = False
           
#             break

#     if is_prime:

#         print(f"{i}-простое число:")

# №2

# Показать на экране таблицу умножения для всех чисел
# от 1 до 10 Например:
# 1 * 1 = 1 1 * 2 = 2 ….. 1 * 10 = 10
# .........................................................................
# 10 * 1 = 10 10 * 2 = 20 …. 10 * 10 = 100


# for x in range(1,11):

#  for y in range(1,11):
#   print(f"{x} * {y} = {x*y}")
#   print()

# №3

# Показать на экран таблицу умножения в диапазоне,
# указанном пользователем. Например, если пользователь
# указал 3 и 5, таблица может выглядеть так
# 3*1 = 3 3*2 = 6 3*3 = 9 ... 3 * 10 = 30
# .....................................................................................
# 5*1 = 5 5 *2 = 10 5 *3 = 15 ... 5 * 10 = 50

# a = int(input("Ведите число которое будет являться начлом диапозонна: "))
# b = int(input("Ведите число которое будет являться концом диапозонна: "))
# for x in range(a,b +1):
#     for y in range(1,11):
#         print(f"{x} * {y} = {x*y}")

# Модуль 3 Циклы.(Часть 5)

# №1
 
# while True:
#     variant = input('Введите вариант от "а" до "к"')
#     length = int(input('Ведите нечётно число'))
#     string = ''
#     for y in range(length):
#         for x in range(length):
#             match variant:
#                 case 'а':
#                     if y <= x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'б':
#                     if y >= x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'в':
#                     if y == x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'г':
#                     if y + x == length - 1:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'д':
#                     if y == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'е':
#                     if y == x or y == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'ж':
#                     if y == x or y == length - 1 - x or y + x == length - 1:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'з':
#                     if y == x or y == length - 1 - x or y + x == length - 1 or y + x == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'и':
#                     if y == x or y == length - 1 - x or y + x == length - 1 or y + x == length - 1 - x or y == length - 1 - x or y + x == length - 1 - x:
#                         string += "*"
#                     else:
#                         string += " "
#                 case 'к':
#                     if y == x or y == length - 1 - x or y + x == length - 1 or y + x == length - 1 - x or y == length - 1 - x or y + x == length - 1 - x or y + x == length - 1 or y + x == length:
#                         string += "*"
#                     else:
#                         string += " "
#                 case _:
#                     pass
#             string += "\n"
#         print(string)


# Модуль 4 Строки. Списки.(Часть 1)

#№1

# Пользователь вводит с клавиатуры строку. Проверьте
# является ли введенная строка палиндромом. Палин-
# дром - слово или текст,которое читаеться одинаково
# слева направо и справа налево. Например, кок; А роза
# упала на лапу Азора; доход; А буду я у дуба.

# def palindrom():

#     string = input("Введите строку: ")

#     string = string.lower()

#     string = string.replace(" ", "")

#     if string == string[::-1]: ## Проверяет, является ли строка такой же, если изменить ее местами,если не находит слово которое не меняеться  то  выводит принт.

#         print("Строка является палиндромом")

#     else:

#         print("Строка не является палиндромом")

# palindrom()

#№2

# Пользователь вводит с клавиатуры некоторый текст,
# после чего пользователь вводит список зарезервированных
# слов. Необходимо найти в тексте все зарезервированные
# слова и изменить их регистр на верхний. Вывести на
# экран измененный текст.

# def palindrom():

#     string = input("Введите строку: ")

    # string = string.lower() ##Получаем вводимые пользователем данные и преобразуем их в нижний регистр

#     string = string.replace(" ", "") ## Убираем пробелы из строки

#     string = string.split()

#     print(string)

#     for i in string:

#         if i in string: ## Проверить, не появляется ли какой-либо символ в строке более одного разадля i в строке:

#             print(i.upper())


# palindrom()

# №3

# Есть некоторый текст. Посчитайте в этом тексте ко-
# личество предложений и выведите на экран полученный
# результат.

# def palindrom():

# string = input("Введите строку: ")

# string = string.lower()##-Метод - lower() ##используется для преобразования строки в нижний регистр.

# string = string.replace(" ", "")##-Метод - replace() ##используется для удаления пробелов из строки.

# string = string.split(".")##-Метод split() ##используется для разделения строки на список подстрок с использованием символа "." в качестве разделителя.

# print(string)##-Функция - print() ##используется для печати списка подстрок и его длины.

# print(len(string))##-Функция - len()## используется для получения длины списка подстрок.



# Модуль 4 Строки. Списки.(Часть 2)





#№1 

# Пользователь вводит с клавиатуры арифметическое
# выражение. Например, 23+12.
# Необходимо вывести на экран результат выражения.
# В нашем примере это 35 Арифметическое выражение
# может состоять только из трёх частей: число, операция,
# число. Возможные операции: +, -,*,/

# def palindrom():

#     string = input("Введите арифметическое выражение: ") ##Предлагает пользователю ввести арифметическое выражение, например "2 + 3" или "4 * 5".

#     string = string.split() ##string = строка.split(): Разбивает входную строку на список слов, используя пробел в качестве разделителя. Например, "2 + 3" станет ["2", "+", "3"].

#     print(string) ##выводит список слов на консоль.

#     print(string[0]+string[2]) ##выводит объединение первого и третьего элементов списка. В приведенном выше примере это означало бы вывод "23".

# palindrom()






# №2
# В списке целых, заполненном случайными числами,
# определить минимальный и максимальный элементы,
# посчитать количество отрицательных элементов, посчи-
# тать количество положительных элементов, посчитать
# количество нулей. Результаты вывести на экран.

# import random

# def palindrom():

#     list = [random.randint(-100, 100) for i in range(21)] ##

#     print(list)

#     print(max(list)) ##выводит максимальный элемент списка.

#     print(min(list)) ##выводит минимальный элемент списка.

#     print(list.count(0)) ##выводит количество нулей в списке.
    
#     countOtr = 0
#     for n in list:
#         if n < 0:
#             countOtr += 1
#     print(countOtr) ##выводит количество отрицательных элементов в списке
    
#     countPol = 0
#     for n in list:
#         if n > 0:
#             countPol += 1
#     print(countPol) ##выводит количество положительных элементов в списке

# palindrom()





# Модуль 4 Строки. Списки.(Часть 3)

# №1 

# Два списка целых заполняются случайными числами.
# Необходимо:
# Сформировать третий список, содержащий элементы
# обоих списков;
# Сформировать третий список, содержащий элементы
# обоих списков без повторений;
# Сформировать третий список, содержащий элементы
# общие для двух списков;
# Сформировать третий список, содержащий только
# уникальные элементы каждого из списков;
# Сформировать третий список, содержащий только
# минимальное и максимальное значение каждого из
# списков



## Два списка целых заполняются случайными числами.
## Необходимо:

# import random
# def task1():
#      print
# list1 = [random.randint(-100, 100) for _ in range(10)]

# list2 = [random.randint(-100, 100) for _ in range(10)]

# print("List 1:", list1)
# print("List 2:", list2)

# # Сформировать третий список, содержащий элементы
# # обоих списков;

# list3 = list1 + list2
# print("List 3:", list3)

# # формировать третий список, содержащий элементы
# # обоих списков без повторений;

# list4 = list(set(list1 + list2))
# print("List 4:", list4)

# # Сформировать третий список, содержащий элементы
# # общие для двух списков;

# list5 = list(set(list1) & set(list2))
# print("List 5:", list5)

# # Сформировать третий список, содержащий только
# # уникальные элементы каждого из списков;

# list6 = list(set(list1) ^ set(list2))
# print("List 6:", list6)
 
# # минимальное и максимальное значение каждого из
# # списков

# list7 = [min(list1), max(list1), min(list2), max(list2)]
# print("List 7:", list7)
# task1()

# Модуль 5 Функции. Функции.(Часть 1)

# №1 

# Задание 1

## Напишите функцию, которая отображает на экран
## форматированный текст, указанный ниже:
## “Don't compare yourself with anyone in this world…
## if you do so, you are insulting yourself.”
##                                           Bill Gates

# print("“Don't compare yourself with anyone in this world…")
# print ("if you do so, you are insulting yourself.”")
# print("                                           Bill Gates")

# Задание 2

## Напишите функцию, которая принимает два числа
## в качестве параметра и отображает все четные числа
## между ними

# def print_even_numbers(a, b):
#     for i in range(a, b+1):
#         if i % 2 == 0:
#             print(i)
# print_even_numbers(1, 10)

# Задание 3

## Напишите функцию, которая отображает пустой или
## заполненный квадрат из некоторого символа. Функция
## принимает в качестве параметров: длину стороны ква-
## драта, символ и переменную логического типа
## если она равна True, квадрат заполненный
## если False, квадрат пустой


## (True или False), указывающую, является ли квадрат
##  пустым или заполненным

# def print_square(size, symbol, is_empty):
#     if is_empty:
#         for i in range(size):
#             if i == 0 or i == size - 1:
#                 print(symbol * size)
#             else:
#                 print(symbol + " " * (size - 2) + symbol)
#     else:
#         for i in range(size):
#             print(symbol * size)
# print_square(5, '*', True)

## Задание 4

## Напишите функцию, которая возвращает минимальное
## из пяти чисел Числа передаются в качестве параметров



# import random 
# import math

# def min_of_five(a, b, c, d, e):
#     return min(a, b, c, d, e)

# print(min_of_five(1, 2, 3, 4, 5))

# print(min_of_five(random.randint(1,5), random.randint(1,5)
                  
# , random.randint(1,5), random.randint(1,5), random.randint
# (1,5)))

# print(min_of_five(math.pi, math.e, math.sqrt(2), math.sqrt(3)
# , math.sqrt(5)))



## Этот код определяет функцию min_of_five, которая принимает пять аргументов и возвращает минимальное значение из них. Затем функция вызывается три раза с разными наборами аргументов:

## С числами 1, 2, 3, 4 и 5.
## С пятью случайными целыми числами от 1 до 5.
## С пятью математическими константами: π, e, √2, √3 и √5.
## Вот краткое описание того, как работает код:

## Первый вызов:


## Печать кода копирования(min_of_five(1, 2, 3, 4, 5))
## Функция min_of_five вызывается с аргументами 1, 2, 3, 4 и 5. Функция min возвращает наименьшее значение из этих аргументов, равное 1. Результатом будет 1.

## Второй вызов:


## Печать кода копирования(min_of_five(random.randint(1,5), random.randint(1,5),
## random.randint(1,5), random.randint(1,5), random.randint(1,5)))
## Функция min_of_five вызывается с пятью случайными целыми числами от 1 до 5. Функция random.randint генерирует случайное целое число от 1 до 5 для каждого аргумента. Функция min возвращает наименьшее значение из этих случайных целых чисел


# import random
# import math

# def min_of_five(args):
#     return min(args)

# print(min_of_five([1, 2, 3, 4, 5]))

# print(min_of_five([random.randint(1,5) for _ in range(5)]))

# print(min_of_five([math.pi, math.e, math.sqrt(2), math.sqrt(3), math.sqrt(5)]))

## Задание 5

## Напишите функцию, которая возвращает произве-
## дение чисел в указанном диапазоне. Границы диапазона
## передаются в качестве параметров. Если границы диапа-
## зона перепутаны (наппример, 5- верхняя граница,25-)
## нижняя граница), их нужно поменять местами

# import math
# def product_of_range(a, b):
#     if a > b:
#         a, b = b, a
#     product = 1
#     for i in range(a, b + 1):
#         product *= i
#     return product
# print(product_of_range(5, 25))
# print(product_of_range(25, 5))

## Задание 6

## Напишите функцию, которая считает количество
## цифр в числе. Число передаётся в качестве параметра. Из
## функции нужно вернуть полученное количество цифр.
## Например, если передали 3456, количество цифр будет 4

# def count_digits(n):
#     return len(str(abs(n)))
# print(count_digits(3456))
# print(count_digits(-3456))

## Задание 7

## Напишите функцию, которая проверяет является ли
## число палиндромом. Число передаётся в качестве пара-
## метра. Если число палиндром нужно вернуть из функции
## true, иначе false.
## «Палиндром» — это число, у которого первая часть
## цифр равна второй перевернутой части цифр. Например,
## 123321 — палиндром (первая часть 123, вторая 321, которая
## после переворота становится 123), 546645 — палиндром,
## а 421987 — не палиндром.

# def is_palindrome(n):
#     return str(n) == str(n)[::-1]
# print(is_palindrome(123321)) # True
# print(is_palindrome(546645)) # True
# print(is_palindrome(421987)) # False



## Модуль 5 Функции. Функции.(Часть 2)

## Задание 1

## Напишите функцию, вычисляющую произведение
## элементов списка целых. Список передаётся в качестве па-
## раметра. Полученный результат возвращается из функции

# def product_of_list(lst):

#     product = 1

#     for i in lst:

#         product *= i

#     return product

# print(product_of_list([1, 2, 3, 4, 5]))


## 1. def product_of_list(lst):: Эта строка определяет функцию с именем product_of_list, которая принимает единственный аргумент lst, представляющий собой список чисел.

## 2. product = 1: В этой строке переменная product инициализируется значением 1. Эта переменная будет использоваться для хранения результатов всех элементов в списке.

## 3. for i в lst:: Эта строка запускает цикл for, который будет выполнять итерацию по каждому элементу i в списке lst.

## 4. product *= i: Внутри цикла эта строка умножает текущее значение product на текущий элемент i. Это делается с помощью оператора *=, который является сокращением от product = продукт * i.

## 5. возвращает product: После того, как цикл завершает итерацию по всем элементам в списке, эта строка возвращает конечное значение product, которое является произведением всех элементов в списке.



## Теперь давайте посмотрим, как эта функция работает с примером входных данных [1, 2, 3, 4, 5]:

## Итерация 1: product = 1 i = 1 product *= 1 => product = 1

## Итерация 2: product = 1 i = 2 product *= 2 => продукт = 2


## Задание 2

## Напишите функцию для нахождения минимума в
## списке целых. Список передаётся в качестве параметра.
## Полученный результат возвращается из функции

# def find_min(lst):

#     return min(lst)

# numbers = [4, 2, 9, 1, 7, 3]

# min_value = find_min(numbers)

# print(min_value)  # Output: 1

## Задание 3

## Напишите функцию, определяющую количество про-
## стых чисел в списке целых. Список передаётся в качестве
## параметра. Полученный результат возвращается из функции

# def count_even_numbers(lst):

#     count = 0

#     for num in lst:

#         if num % 2 == 0:

#             count += 1

#     return count

# numbers = [1, 2, 3, 4, 5, 6]

# even_count = count_even_numbers(numbers)

# print(even_count)  # Output: 3

## Задание 4

## Напишите функцию, удаляющую из списка целых
## некоторое заданное число. Из функции нужно вернуть
## количество удаленных элементов

# def remove_number(lst, num):

#     count = 0

#     for i in range(len(lst) - 1, -1, -1):

#         if lst[i] == num:

#             lst.pop(i)

#             count += 1

#             return count
        
#         return count
    
#     numbers = [1, 2, 2, 3, 2, 4,]

#     removed_count = remove_number(numbers, 2)

#     print(removed_count)  # Output: 3

## Задание 5

## Напишите функцию, которая получает два списка в
## качестве параметра и возвращает список, содержащий
## элементы обоих списков

# def merge_lists(list1, list2):

#     return list1 + list2

# list1 = [1, 2, 3]

# list2 = [4, 5, 6]

# print(merge_lists(list1, list2))  # Output: [1, 2,]


## Задание 6

## Напишите функцию, высчитывающую степень каждого
## элемента списка целых. Значение для степени передаётся
## в качестве параметра, список тоже передаётся в качестве
## параметра. Функция возвращает новый список, содержа-
## щий полученные результаты

# def merge_lists(lst):

#     return [i**2 for i in lst]

# def power_list(lst, power):
         
#          return [i**power for i in lst]

# list1 = [1, 2, 3, 4, 5]

# print(power_list(list1, 2))  # Output: [1, 4, 9]

    
## Модуль 5 Функции. Функции.(Часть 3)
    
## Задание 1
## Написать рекурсивную функцию нахождения наи-
## большего общего делителя двух целых чисел

# def gcd(a, b):

#     if b == 0:

#         return a
    
#     else:

#         return gcd(b, a % b) 
    
# print(gcd(12, 15))  # Output: 3


# Задание 2

# Написать игру «Быки и коровы». Программа «за-
# гадывает» четырёхзначное число и играющий должен
# угадать его. После ввода пользователем числа программа
# сообщает, сколько цифр числа угадано (быки) и сколько
# цифр угадано и стоит на нужном месте (коровы). После
# отгадывания числа на экран необходимо вывести коли-
# чество сделанных пользователем попыток. В программе
# необходимо использовать рекурсию

# import random

# def game():

#     number = str(random.randint(1000, 9999))  # загадываем число

#     attempts = 0

#     while True:

#         guess = input("Введите четырёхзначное число: ")

#         if len(guess) != 4 or not guess.isdigit():

#             print("Некорректный ввод. Введите четырёхзначное число")

#             continue

#         attempts += 1

#         bulls = 0

#         cows = 0

#         for i in range(4):

#             if guess[i] == number[i]:

#                 bulls += 1

#             elif guess[i] in number:
             
#              cows += 1

#             print(f"Быки: {bulls}, Коровы: {cows}")

#             if bulls == 4:
             
#              print(f"Вы угадали! Количество попыток: {attempts}")
#             break
        
# game() # запуск игры

        

## Вот пошаговое объяснение того, как работает код:

## 1. Импорт модуля random

## Код начинается с импорта модуля random, который используется для генерации случайного числа.

## 2. Определение функции game()

## Определена функция game(), которая будет содержать логику игры.

## 3. Генерация случайного числа

## Переменной number задается случайное четырехзначное число с помощью random.randint(1000, 9999). Это число будет секретным номером, который пользователь должен угадать.

## 4. Инициализация переменной attempts

## Переменной attempts присваивается значение 0, которое будет отслеживать количество попыток пользователя угадать число.

## 5. Вход в игровой цикл

## Код переходит в бесконечный цикл, используя while True:. Этот цикл будет продолжаться до тех пор, пока пользователь правильно не угадает число.

## 6. Получение пользовательского ввода

## Пользователю предлагается ввести четырехзначное число с помощью ввода("Введите значение: "). Введенные данные сохраняются в переменной guess.

## 7. Проверка правильности ввода пользователем

## Код чепроверьте правильность введенных пользователем данных, проверив, составляет ли длина введенных данных 4 символа и все ли символы являются цифрами, используя len(угадайте) != 4 или не угадывайте.isdigit(). Если вводимые данные неверны, выводится сообщение об ошибке, и цикл продолжается.

## 8. Увеличение переменной attempts

## Если вводимые данные верны, переменная attempts увеличивается на 1.

## 9. Инициализация переменных bulls и cows

## Переменным bulls и cows присваивается значение 0. Эти переменные будут использоваться для отслеживания количества правильных цифр в правильном положении (bulls) и количества правильных цифр в неправильном положении (cows).

## 10. Сравнение догадки с секретным номером

## Код повторяет каждую цифру предположения и сравнивает ее с соответствующей цифрой секретного номера, используя значение для i в диапазоне(4):. Если цифра совпадает в точности, это увеличивает значение переменной bulls. Если в секретном номере присутствует цифра, но она находится в неправильном положении, значение переменной cows увеличивается.

## 11. Вывод результата на печать

## Код выводит количество быков и коров с помощью print(f"Быки: {быки}, Коровы: {коровы}").

## 12. Проверяем, выиграл ли пользователь

## Если количество буллов равно 4, это означает, что пользователь правильно угадал число, и игра выиграна. Код выводит поздравительное сообщение с количеством попыток, сделанных с помощью print("Спасибо! Количество попыток: {attempts}").

## 13. Выход из цикла

## Если пользователь выиграл, код выходит из цикла с помощью break.

## 14. Запуск игры

## Наконец, для запуска игры вызывается функция game().

## Задание 4
## Написать игру «Пятнашки».

def game():
    import random

# Заготовки для отображения поля
up = """+-----+-----+-----+-----+
|     |     |     |     |"""
mid = """|     |     |     |     |
+-----+-----+-----+-----+
|     |     |     |     |"""
bot = """|     |     |     |     |
+-----+-----+-----+-----+"""

def get_new_random():
    line = list(range(16))
    random.shuffle(line)
    return line

def print_board(new_game):
    print(up)
    for i in range(0, 16):
        if new_game[i]<10:
            if new_game[i] == 0:
                print('| ', end = '')
            else:
                print('| '+str(new_game[i])+' ', end = '')
        else:
            num = str(new_game[i])
            print('| '+num[0]+' '+num[1]+' ', end = '')
        if i == 3 or i == 7 or i == 11:
            print('|')
            print(mid) 
    print('|')
    print(bot)

def ansver():
    while True:
        text = input('Введите число от 1 до 15:')
        if text.isdigit() == False:
            print('Вводите только целые числа!')
        elif 15<int(text) or int(text)<0:
            print('Нет такого числа на игровом поле!')
        else:
            return int(text)

def possible_moves(new_game):
    moves = []
    ind = new_game.index(0)
    if ind == 0:
        moves.append(new_game[1])
        moves.append(new_game[4])
    elif ind == 1:
        moves.append(new_game[0])
        moves.append(new_game[2])
        moves.append(new_game[5])
    elif ind == 2:
        moves.append(new_game[1])
        moves.append(new_game[3])
        moves.append(new_game[6])
    elif ind == 3:
        moves.append(new_game[2])
        moves.append(new_game[7])
    elif ind == 4:
        moves.append(new_game[0])
        moves.append(new_game[5])
        moves.append(new_game[8])
    elif ind == 5:
        moves.append(new_game[1])
        moves.append(new_game[4])
        moves.append(new_game[6])
        moves.append(new_game[9])
    elif ind == 6:
        moves.append(new_game[2])
        moves.append(new_game[5])
        moves.append(new_game[7])
        moves.append(new_game[10])
    elif ind == 7:
        moves.append(new_game[3])
        moves.append(new_game[6])
        moves.append(new_game[11])
    elif ind == 8:
        moves.append(new_game[4])
        moves.append(new_game[9])
        moves.append(new_game[12])
    elif ind == 9:
        moves.append(new_game[5])
        moves.append(new_game[8])
        moves.append(new_game[10])
        moves.append(new_game[13])
    elif ind == 10:
        moves.append(new_game[6])
        moves.append(new_game[9])
        moves.append(new_game[11])
        moves.append(new_game[14])
    elif ind == 11:
        moves.append(new_game[7])
        moves.append(new_game[10])
        moves.append(new_game[15])
    elif ind == 12:
        moves.append(new_game[8])
        moves.append(new_game[13])
    elif ind == 13:
        moves.append(new_game[9])
        moves.append(new_game[12])
        moves.append(new_game[14])
    elif ind == 14:
        moves.append(new_game[10])
        moves.append(new_game[13])
        moves.append(new_game[15])
    else:
        moves.append(new_game[11])
        moves.append(new_game[14])
    return moves

# Основной код игры
win = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,0]
new_game = get_new_random()
print_board(new_game)

while True:
    moves = possible_moves(new_game)
    move_num = ansver()
    if move_num in moves:
        ind_move = new_game.index(move_num)
        ind_0 = new_game.index(0)
        new_game[ind_0] = move_num
        new_game[ind_move] = 0
        print_board(new_game)
    else:
        print('Это число нельзя переместить!')
    if new_game == win:
        print('Поздравляю! Вы победили!')
        break