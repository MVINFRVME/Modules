

class Parent:

    def __init__(self, name, age, children):
        self.name = name
        self.age = age
        self.children = children

    def show_info(self):
        print(f'Имя: {self.name}\n'
              f'Возраст: {self.age}\n'
              f'Список детей:', end='')
        for my_child in self.children:
            print(my_child.name, end=' ')
        print()

    def calm_down(self):
        for child in self.children:
            if child.mind_state < 2:
                child.mind_state += 1
                print(f'Успокаиваем... {child.name} теперь {child.mind_states[child.mind_state]}')
            else:
                print(f'{child.name} уже {child.mind_states[child.mind_state]}')

    def feed(self):
        for child in self.children:
            if child.hunger_state < 3:
                child.hunger_state += 1
                print(f'Кормим...{child.name} теперь {child.hunger_states[child.hunger_state]}')
            else:
                print(f'{child.name} {child.hunger_states[child.hunger_state]}')


class Child:
    # очень похоже что ты не будешь изменять эти аттрибуты в процессе выполнения программы,
    # значит это константы, константы пишут капсом

    hunger_states = {0: 'очень голодный', 1: 'голодный', 2: 'слегка голоден', 3: 'сытый'}
    mind_states = {0: 'плачет', 1: 'обеспокоен', 2: 'спокоен'}

    def __init__(self, name, age, hunger_state=0, mind_state=0):
        self.name = name
        self.age = age
        self.hunger_state = hunger_state
        self.mind_state = mind_state
