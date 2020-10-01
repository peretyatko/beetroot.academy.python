'''School

Make a class structure in python representing people at school. Make a base class called Person,
a class called Student, and another one called Teacher. Try to find as many methods and attributes
as you can which belong to different classes, and keep in mind which are common and which are not.
For example, the name should be a Person attribute, while salary should only be available to the teacher. '''




class Person():
    def __init__(self, first_name, last_name, year, eyes_color):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.eyes_color = eyes_color


class Student(Person):
    def __init__(self, first_name, last_name, year, eyes_color, acad_perf, hair_color):
        super().__init__(first_name, last_name, year, eyes_color)
        self.acad_perf = acad_perf
        self.hair_color = hair_color

    def ball_of_acad_pref(self, num_of_ball = 1):
        self.acad_perf += num_of_ball

    def repaint(self, new_hair_color):
        self.hair_color = new_hair_color


class Teacher(Person):
    salary = 4000
    def __init__(self, first_name, last_name, year, eyes_color, salary, degree):
        super().__init__(first_name, last_name, year,eyes_color)

        self.salary = salary
        self.degree = degree

    def teacher_salary(self, bonus):
        self.salary += bonus

    def teacher_degree(self, new_degree):
        self.degree = new_degree


rik = Teacher('Rik', 'Morty', 30, 'green', 4000, 'master')
ross = Student('Ross', 'Geller', 13, 'blue', 90, 'red')
print(rik.salary)
print(rik.degree)
rik.teacher_degree('professor')
print(rik.degree)
rik.teacher_salary(8000)
print(rik.salary)


print(ross.acad_perf)
ross.ball_of_acad_pref(5)
print(ross.acad_perf)
print(ross.hair_color)
ross.repaint('blue')
print(ross.hair_color)

print(rik.hair_color)
print(ross.degree)