class Person:
    def __init__(self, name, last_name, id_number, age):
        self.name = name
        self.last_name = last_name
        self.__id_number = id_number
        self._age = age

    def info_person(self):
        return self.name, self.last_name, self.__id_number, self._age

    def get_age(self):
        print (self._age)

    def get_id_number(self):
        print (self.__id_number)

    def get_full_name(self):
        print (self.name, self.last_name)


    def set_age(self, age):
        if age in range(1, 150):
            self._age = age
        else:
            print('Должно быть положительным числом')

    def set_name(self, name):
        print (self.name)



class Director(Person):
    def __init__(self, name, last_name, id_number, age):
        super().__init__(name, last_name, id_number, age)




class Teacher(Person):
    def __init__(self, name, last_name, id_number, age):
        super().__init__(name, last_name, id_number, age)



class Student(Person):
    def __init__(self, name, last_name, id_number, age):
        super().__init__(name, last_name, id_number, age)


