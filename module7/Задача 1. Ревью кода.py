# Задача 1. Ревью кода
# Что нужно сделать
# Ваня работает middle-разработчиком на Python в IT-компании. Один кандидат на позицию junior-разработчика прислал ему
# код тестового задания. В задании был словарь из трёх студентов. Необходимо:
#
# Вывести на экран список пар «ID студента — возраст».
# Написать функцию, которая принимает в качестве аргумента словарь и возвращает два значения: полный список интересов
# всех студентов и общую длину всех фамилий студентов.
# Далее в основном коде вызывается функция, значения присваиваются отдельным переменным и выводятся на экран.
#
# Ваня — очень придирчивый программист, и после просмотра кода он понял, что этого кандидата на работу не возьмёт, хотя
# код выдаёт верный результат. Вот код кандидата:

# students = {
# 1: {
# 'name': 'Bob',
# 'surname': 'Vazovski',
# 'age': 23,
# 'interests': ['biology, swimming']
# },
# 2: {
# 'name': 'Rob',
# 'surname': 'Stepanov',
# 'age': 24,
# 'interests': ['math', 'computer games', 'running']
# },
# 3: {
# 'name': 'Alexander',
# 'surname': 'Krug',
# 'age': 22,
# 'interests': ['languages', 'health food']
# }
# }

# def f(d:dict):
#     interests = set()
#     common_last_name_lenght = 0
#
#     for id, student_info in students.items():
#         print(id, student_info['age'])
#
#         interests.update(student_info['interests'])
#         common_last_name_lenght += len(student_info['surname'])
#     return interests, common_last_name_lenght
# students = {
# 1: {
# 'name': 'Bob',
# 'surname': 'Vazovski',
# 'age': 23,
# 'interests': ['biology, swimming']
# },
# 2: {
# 'name': 'Rob',
# 'surname': 'Stepanov',
# 'age': 24,
# 'interests': ['math', 'computer games', 'running']
# },
# 3: {
# 'name': 'Alexander',
# 'surname': 'Krug',
# 'age': 22,
# 'interests': ['languages', 'health food']
# }
# }
#
# def f(dict):
# lst = []
# string = ''
# for i in dict:
# lst += (dict[i]['interests'])
# string += dict[i]['surname']
# cnt = 0
# for s in string:
# cnt += 1
# return lst, cnt
#
# pairs = []
# for i in students:
# pairs += (i, students[i]['age'])
#
# my_lst = f(students)[0]
# l = f(students)[1]
# print(my_lst, l)

# Перепишите этот код так, чтобы он был максимально pythonic и Ваня мало к чему мог придраться (только если очень
# захочется). Убедитесь, что программа верно работает. Проверки на существование записей в словаре не обязательны, но
# приветствуются.
#
# Результат работы программы:
# Список пар «ID студента — возраст»: [(1, 23), (2, 24), (3, 22)]
# Полный список интересов всех студентов:
# {'running', 'computer games', 'math', 'languages', 'biology, swimming', 'health food'}
# Общая длина всех фамилий студентов: 20
#
# Советы и рекомендации
# Обратите внимание на нейминг — имена переменных и функций должны быть полезными и понятными (не стоит использовать
# одиночные буквы, непонятные сокращения). Названия не должны пересекаться с уже существующими в Python объектами
# (например, лучше не называть свою переменную print или list).
# Попробуйте найти лишние действия в коде. Если вы сможете получить нужный результат меньшим количеством действий, то
# не нужно заставлять Python выполнять лишние действия. Также нет необходимости заставлять Python выполнять одни и те
# же действия над одним и тем же объектом (например, вызывать функцию с одними и теми же входными данными несколько раз)
# .

students = {
            1: {
                'name': 'Bob',
                'surname': 'Vazovski',
                'age': 23,
                'interests': ['biology, swimming']
                },

            2: {
                'name': 'Rob',
                'surname': 'Stepanov',
                'age': 24,
                'interests': ['math', 'computer games', 'running']
                },

            3: {
                'name': 'Alexander',
                'surname': 'Krug',
                'age': 22,
                'interests': ['languages', 'health food']
                }
            }


def surname_len_and_interests(data):
    stud_interests = set()
    letter_count = 0
    for id_student in data.values():
        stud_interests.update(id_student['interests'])
        letter_count += len(id_student['surname'])

    return set(stud_interests), letter_count # todo тут set можно убрать теперь


pairs = [(id_num, info['age']) for id_num, info in students.items()]

interests, surnames_length = surname_len_and_interests(students)

print(f'Список пар «ID студента — возраст»: {pairs}\n'
      f'Полный список интересов всех студентов: {interests}\n'
      f'Общая длина всех фамилий студентов: {surnames_length}')

# ok
