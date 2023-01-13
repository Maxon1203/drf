# class Employee:       # определение класса Person


#     def hello_emp(self, name, group):
#         name = "SANE"
#         group = "pasds"
#         self.name = name
#         self.group = group
#         # print(f"Привет {self.name} из группы {self.group}")
#     def Colledg (self):
#          print(f"Привет {self.name} из группы {self.group} из MPT")

# Max = Employee()
# Max.hello_emp("","")
# Max.Colledg()

# Наследование
# class Employee:       # определение класса Employee
    
#     # Конструктор
#     def __init__(self, name, group):
#         self.n = name
#         self.g = group
#         self.a = 15

#     # def __str__(self) -> str:
#     #     return "Привет"   

# class Work(Employee):
#     def __init__(self, name, group):
#         # связывает потомка с родителем 
#         super().__init__(name, group) # обращение к методу __init__ в классе Employee
#         print(f"Привет {self.n} из группы {self.g} возраст {self.a}")

# Max = Work("Max","MPT")    # Привет Max из группы MPT возраст 15
# print(Max)              # Привет Max из группы MPT возраст 15

#     @property
#     def Name(self):
#         return self.__name
 
#     def do_nothing(self):
#         print(f"{self.Name} ничего не делает")
 
 
# #  класс работника
# class Employee(Person):
 
#     def work(self):
#         print(f"{self.Name} работает")
 
 
# #  класс студента
# class Student(Person):
 
#     def study(self):
#         print(f"{self.Name} студент")
 
# #  проверяем к какому классу принадлежит тот или иной человек
# def proverka(person):
#     if isinstance(person, Student):
#         person.study()
#     elif isinstance(person, Employee):
#         person.work()
#     elif isinstance(person, Person):
#         person.do_nothing()
 
 
# tom = Employee("Tom")
# bob = Student("Bob")
# sam = Person("Sam")
 
# proverka(tom)    # Tom работает
# proverka(bob)    # Bob студент
# proverka(sam)    # Sam ничего не делает

class PersonAgeException(Exception):
    def __init__(self, age, minA, maxA):
        self.age = age
        self.minAge = minA
        self.maxAge = maxA
    
    def __str__(self):
        return f"Недопустимое значение: {self.age}. " \
               f"Возраст должен быть в диапазоне от {self.minAge} до {self.maxAge}"

class Person:
 
    def __init__(self, name, age):
        self.__name = name   # имя человека
        maxAge, minAge = 150,1
        if minAge < age < maxAge:
            self.__age = age        # устанавливаем возраст, если передано корректное значение
        else:
            raise PersonAgeException(age, minAge, maxAge)   # иначе генерируем исключение
    def info(self):
        print(f"Вас зовут {self.__name} вам {self.__age} лет",)
   # Недопустимое значение: -23. Возраст должен быть в диапазоне от 1 до 160