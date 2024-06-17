# Задача 2. Студенты
# Что нужно сделать
# Реализуйте модель с именем Student, содержащую поля «ФИ», «Номер группы», «Успеваемость» (список из пяти элементов).
# Затем создайте список из десяти студентов (данные о студентах можете придумать или запросить у пользователя) и
# отсортируйте список по возрастанию среднего балла. Выведите результат на экран.

class Student:

    def __init__(self, name, group_num, grades: list):
        self.name = name
        self.group_num = group_num
        self.grades = grades


students = [Student('Ivanov Ivan', 1, [5, 4, 4, 3, 4]),
            Student('Petrov Petr', 1, [3, 4, 3, 3, 4]),
            Student('Sidorov Sidor', 2, [4, 4, 5, 4, 4]),
            Student('Kozlov Kozel', 2, [5, 5, 5, 5, 5]),
            Student('Ivanova Irina', 1, [1, 1, 1, 1, 1]),
            Student('Petrova Polina', 3, [5, 5, 4, 5, 5]),
            Student('Sidorova Svetlana', 3, [3, 4, 4, 4, 4]),
            Student('Kozlova Kristina', 2, [5, 5, 5, 5, 5]),
            Student('Ivan Ivanov', 4, [4, 4, 3, 4, 4]),
            Student('Petr Petrov', 4, [5, 5, 5, 5, 5])]

for i_student in students: # я бы назвал просто student, будет выглядеть чище
    cur_grades = 0
    for grade in i_student.grades:
        cur_grades += grade
    i_student.grades = cur_grades / len(i_student.grades)

sorted_students = sorted(students, key=lambda x: x.grades)

for i_student in sorted_students:
    print(f'Студент: {i_student.name}, группа: {i_student.group_num}, средний бал: {i_student.grades}')

# ok
