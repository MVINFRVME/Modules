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

def f(d:dict):
    interests = set()
    common_last_name_lenght = 0

    for id, student_info in students.items():
        print(id, student_info['age'])

        interests.update(student_info['interests'])
        common_last_name_lenght += len(student_info['surname'])
    return interests, common_last_name_lenght
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


def func(students_dict): # todo func не особо говорящее имя, попробуй заменить на описание того что она делает, если будет несколько слов это ок
    interest_list = list() # todo обычно для словарей, списков и т.п. используют множественное число того что содержится внутри, а не приставка list\dict\etc
    letter_count = 0
    for i_key in students_dict.values(): # todo для переменной цикла хочется более говорящее имя
        interest_list += i_key['interests']
        letter_count += len(i_key['surname'])

    return set(interest_list), letter_count # todo c set хорошо придумал, а можно сразу его использовать?


pairs = list() # todo тут все отлично, но вообще можно заменить на list comprehensions
for id_num, info in students.items():
    pair = (id_num, info['age'])
    pairs.append(pair)

interests, surnames_length = func(students)

print(f'Список пар «ID студента — возраст»: {pairs}\n'
      f'Полный список интересов всех студентов: {interests}\n'
      f'Общая длина всех фамилий студентов: {surnames_length}')
