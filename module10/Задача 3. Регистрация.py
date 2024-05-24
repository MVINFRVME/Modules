# Задача 3. Регистрация
# Что нужно сделать
# У вас есть файл с протоколом регистрации пользователей на сайте — registrations.txt. Каждая строка содержит имя, имейл
# и возраст, разделённые пробелами. Например: Василий test@test.ru 27.

# Напишите программу, которая проверяет данные из файла для каждой строки:

# Присутствуют все три поля.
# Поле «Имя» содержит только буквы.
# Поле «Имейл» содержит @ и точку.
# Поле «Возраст» представляет число от 10 до 99.
# В результате проверки сформируйте два файла:

# registrations_good.log для правильных данных; записывать строки как есть;
# registrations_bad.log — для ошибочных; записывать строку и вид ошибки.
# Для валидации строки данных напишите функцию, которая может выдавать исключения:

# НЕ присутствуют все три поля: IndexError.
# Поле «Имя» содержит НЕ только буквы: NameError.
# Поле «Имейл» НЕ содержит @ и точку: SyntaxError.
# Поле «Возраст» НЕ представляет число от 10 до 99: ValueError.
# Формат выходных данных

# Содержимое файла registrations_bad.log:
# Ольга kmrn@gmail.com 123        Поле «Возраст» НЕ представляет число от 10 до 99
# Чехова kb@gmail.com 142        Поле «Возраст» НЕ представляет число от 10 до 99
# ……
# Степан ky 59        Поле «Имейл» НЕ содержит @ и точку
# ……

# Содержимое файла registrations_good.log:
# Геннадий ttdababmt@gmail.com 69
# Ольга ysbxur@gmail.com 20
# ……

# Советы и рекомендации
# Помните, что пайтон не всегда будет выполнять операции, которые вы предполагали, например:
# if '1' and '2' in строка — по приоритету операций сперва будет выполнено действие с in, а уже потом and. Значит,
# пайтон не будет в этом случае искать 1 внутри строки. Элементы а, б, с: разделять объект (например, список) на
# несколько переменных очень удобно при помощи множественного присваивания. Но если элементов в списке окажется меньше,
# чем указанных переменных, то появится ошибка. При необходимости вы можете объединять исключения в except-блоке. Для
# этого нужно перечислить классы исключений, которые вы хотите отследить в кортеже:  except (DrunkError,
# CarCrashError...) as exc
# As exc в данном случае сработает так же, как и с файлами в конструкции with open(...) as file. То есть пайтон запишет
# пойманное исключение в переменную с названием exc (название может быть любым). При переезде зачастую нужно вынести
# много коробок с вещами из дома. Если для переноса каждой коробки придётся открывать/закрывать двери, то на это уйдет
# много сил. Их уйдет меньше, если получится открыть двери один раз и закрыть, когда всё будет сделано. То же самое
# справедливо и для файлов. Старайтесь открывать и закрывать их экономно, например, открыть файлы можно до цикла, а
# закрыть — после (если нет необходимости переоткрывать файл внутри цикла).

def is_valid_data(info):
    for line in info:
        clear_data = line.rstrip().split()
        try:
            if len(clear_data) != 3:
                raise IndexError
            name, email, age = clear_data
            if name_check(name, clear_data):
                if email_check(email, clear_data):
                    if age_check(age, clear_data):
                        registrations_good_file.write(line)

        except IndexError:
            error_text = f'{clear_data}       НЕ присутствуют все три поля.\n'
            registrations_bad_file.write(error_text)


def name_check(name, clear_data):
    try:
        if not name.isalpha():
            raise NameError
        else:
            return True
    except NameError:
        error_text = f'{clear_data}        Поле «Имя» содержит НЕ только буквы.\n'
        registrations_bad_file.write(error_text)
        return False


def email_check(email, clear_data):
    try:
        if '@' not in email:
            raise SyntaxError
        elif '.' not in email:
            raise SyntaxError
        else:
            return True
    except SyntaxError:
        error_text = f'{clear_data}        Поле «Имейл» НЕ содержит @ и точку.\n'
        registrations_bad_file.write(error_text)
        return False


def age_check(age, clear_data):
    try:
        if not 10 <= int(age) <= 99:
            raise ValueError
        else:
            return True
    except ValueError:
        error_text = f'{clear_data}        Поле «Возраст» НЕ представляет число от 10 до 99.\n'
        registrations_bad_file.write(error_text)
        return False


with open('registrations.txt', 'r', encoding='utf-8') as user_info:
    with open('registrations_good.log', 'w', encoding='utf-8') as registrations_good_file:
        with open('registrations_bad.log', 'w', encoding='utf-8') as registrations_bad_file:
            is_valid_data(user_info)
