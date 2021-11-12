from main import *
person = Person(' ', ' ', ' ', ' ')

director = Director('Ivan', 'Petrov', 12364587987, 45)
director2 = Director('Maksim', 'Ivanov', 154875696, 50)


teacher = Teacher('Anna', 'Gudkova', 15566569, 36)
teacher2 = Teacher('Olga', 'Samoilova', 1236548965, 40)

student = Student('Samara', 'Melisova', 12365583, 22)
student2 = Student('Nazira', 'Toktomuratova', 12366549, 20)



persons = [director, director2, teacher, teacher2, student, student2]
for i in persons:
    print(i.info_person())


director.set_age(35)
director.set_name('Maksim')

director.get_age()
director.get_id_number()
director.get_full_name()


director2.get_age()
director2.get_id_number()
director2.get_full_name()


teacher.get_age()
teacher.get_id_number()
teacher.get_full_name()


teacher2.get_age()
teacher2.get_id_number()
teacher2.get_full_name()


student.get_age()
student.get_id_number()
student.get_full_name()


student2.get_age()
student2.get_id_number()
student2.get_full_name()




