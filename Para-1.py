from Class import method
from Class import classTest

# Ввод данных
name = input("Введите ваше имя:")
age = input("Введите ваш возраст:")
# Вывод в консоль
# Обьединение строк
print("Привет: ",name, "Возраст: ",age)
# Вывод через форматирование строки
print(f"Hello {name} возраст {age}")


# number = input("Кол-во чисел: ") 
# znak = input("Введите знак: ")
# if (znak == "+"):
#     i=1
#     summ = 0
#     while i <= int(number):
#         i +=1
#         numbers = input("число")
#         summ += int(numbers)
#     print(summ)
# elif(znak =="-"):
#     i=1
#     summ = 0
#     while i <= int(number):
       
#         numbers = input("число")
#         if (i == 1):
#             summ = int(numbers)           
#         else:
#             summ -=int(numbers)
#         i +=1

#     print(summ)
# elif(znak =="*"):
#     i=1
#     summ = 1
#     while i <= int(number):
#         i +=1
#         numbers = input("число")
#         summ *= int(numbers)
#     print(summ)
 
# Плюс
# print(12 + 2)  #14
# # Минус
# print(5 - 2)  #3
# # Умножение
# print(4 * 2)  #8
# # Деление 
# print(5 / 2)  #2.5
# # Деление с остатком
# print(5 // 2)  #2
# # Округление 
# print(round(7 / 3, 3))  #2.333

# def sum(numbers):
#     result=0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}") 

# number = input("Кол-во чисел: ") 
# i=1
# qwe = []
# while i <= int(number):
#     i +=1
#     numbers = input("число")
#     qwe.append(int(numbers))
# sum(qwe)

# def testParam(name, age = 222, /, *, company):
#     print(f"Name: {name}  Age: {age}  Company: {company}")
 
 
# testParam("Victor", 16, company ="Google")               
# testParam("Alex", 37, company ="MPT")        
# testParam("Bin",company ="REY",)

# def Summ(*numbers):
#     print(numbers)

# users = {
#     "Tom": {
#         "phone": "+971478745",
#         "email": "tom12@gmail.com"
#     },
#     "Bob": {
#         "phone": "+876390444",
#         "email": "bob@gmail.com",
#         "skype": "bob123"
#     }
# }

# Max = classTest.Employee("Max","P50-3-252")    # Чао
# print(Max.say_hello())              # Привет Max из группы P50-3-252 возраст 22
# # print(users.keys())
# for key in users.keys():
#     if key == "Tom":
#         print(users["Tom"]["email"])
# else:
#     print("skype is not found")

# Summ(23,42,25,2,1,5,14,1)
# def sum(numbers):
#     result=0
#     for n in numbers:
#         result += n
#     print(f"sum = {result}") 
# try:
#     number1 = int(input("Введите первое число: "))
#     number2 = int(input("Введите второе число: "))
#     if number2 <= 5:
#         raise Exception("Второе число не должно быть меньше или равно 5")
#     print("Результат деления двух чисел:", number1/number2)
# except ValueError:
#     print("Введены некорректные данные")
# except Exception as e:
#     print(e)
# finally:
#     print("Завершение программы")
# try:
#     TestExc = classTest.Person("Victor", 11)
#     TestExc.info()  # Имя: Victor  Возраст: 11
 
#     TestExc2 = classTest.Person("Alex", -3)  # генерируется исключение типа PersonAgeException
#     TestExc2.info()
# except classTest.PersonAgeException as e:
#     print(e) 