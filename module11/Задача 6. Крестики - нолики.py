# Задача 6. Крестики-нолики
# Что нужно сделать
# Создайте программу, которая реализует игру «Крестики-нолики».
# Для этого напишите:

# 1. Класс, который будет описывать поле игры.
# class Board:
     #  Класс поля, который создаёт у себя экземпляры клетки.
     #  Пусть класс хранит информацию о состоянии поля (это может быть список из девяти элементов).
     #  Помимо этого, класс должен содержать методы:
     #  «Изменить состояние клетки». Метод получает номер клетки и, если клетка не занята, меняет её состояние. Если
# состояние удалось изменить, метод возвращает True, иначе возвращается False.
     #  «Проверить окончание игры». Метод не получает входящих данных, но возвращает True/False. True — если один из
#  игроков победил, False — если победителя нет.

# 2. Класс, который будет описывать одну клетку поля:
# class Cell:
     #  Клетка, у которой есть значения:
     #  занята она или нет;
     #  номер клетки;
     #  символ, который клетка хранит (пустая, крестик, нолик).

# 3. Класс, который описывает поведение игрока:
# class Player:
     #  У игрока может быть:
     #  имя,
     #  количество побед.

     #  Класс должен содержать метод:
     #   «Сделать ход». Метод ничего не принимает и возвращает ход игрока (номер клетки). Введённый номер нужно
#   обязательно проверить.

# 4. Класс, который управляет ходом игры:
# class Game:
     # класс «Игры» содержит атрибуты:
     # состояние игры,
     # игроки,
     # поле.

     # А также методы:
     # Метод запуска одного хода игры. Получает одного из игроков, запрашивает у игрока номер клетки, изменяет поле,
# проверяет, выиграл ли игрок. Если игрок победил, возвращает True, иначе False.
     # Метод запуска одной игры. Очищает поле, запускает цикл с игрой, который завершается победой одного из игроков или
# ничьей. Если игра завершена, метод возвращает True, иначе False.
     # Основной метод запуска игр. В цикле запускает игры, запрашивая после каждой игры, хотят ли игроки продолжать
# играть. После каждой игры выводится текущий счёт игроков.


class Board:
    def __init__(self):
        self.cells = [Cell(i) for i in range(1, 10)]

    def board_state(self):
        print()
        for i, cell in enumerate(self.cells):
            print(f'|{cell.symbol}', end='')
            if (i + 1) % 3 == 0:
                print('|\n')

    def change_cell_state(self, cell_num, symbol):
        if self.cells[cell_num].symbol == ' ':
            self.cells[cell_num].symbol = symbol
            return True
        else:
            return False

    def is_victory(self):
        for i in range(0, 7, 3):
            if (self.cells[i].symbol == self.cells[i + 1].symbol == self.cells[i + 2].symbol
                    and self.cells[i].symbol != ' '):
                return True
        for i in range(3):
            if (self.cells[i].symbol == self.cells[i + 3].symbol == self.cells[i + 6].symbol
                    and self.cells[i].symbol != ' '):
                return True
        if (self.cells[0].symbol == self.cells[4].symbol == self.cells[8].symbol
                and self.cells[0].symbol != ' '):
            return True
        if (self.cells[2].symbol == self.cells[4].symbol == self.cells[6].symbol
                and self.cells[2].symbol != ' '):
            return True

        return False


class Cell:
    def __init__(self, num):
        self.num = num
        self.symbol = ' '


class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.victory_count = 0
        self.symbol = symbol

    def make_a_move(self):
        try:
            cell_num = int(input(f'{self.name}, введите номер клетки (1 - 9): '))

            while not 1 <= cell_num <= 9:
                print('Неверное значение! Введите номер от 1 до 9!')
                return self.make_a_move()

        except ValueError:
            print('Используйте только цифры!')
            return self.make_a_move()

        return cell_num
    # todo вообще норм, но рекурсия выглядит переусложнением, можно сделать бесконечный цикл, проверять строку на то что это число, потом что значение от 1 до 9


class Game:
    def __init__(self, player_one, player_two):
        self.player_one = player_one
        self.player_two = player_two
        self.board = Board()
        self.cur_player = player_one

    def one_turn(self):
        cell_num = self.cur_player.make_a_move()

        if game.board.change_cell_state(cell_num - 1, self.cur_player.symbol):
            self.board.board_state()
        else:
            print('Эта клетка уже занята!')
            return self.one_turn()

        if self.board.is_victory():
            return True

        if self.cur_player == self.player_one:
            self.cur_player = self.player_two
        else:
            self.cur_player = self.player_one

    def one_game(self):
        for _ in range(9):
            if self.one_turn():
                print(f'Игра окончена. Победил {self.cur_player.name}!')
                self.cur_player.victory_count += 1
                return True
        print('Ничья!')
        return True

    def start_game(self):
        if self.one_game():
            print(f'Счёт по партиям:\n'
                  f'{self.player_one.name} - {self.player_one.victory_count} побед\n'
                  f'{self.player_two.name} - {self.player_two.victory_count} побед\n')
        while True:
            is_continue = input('Хотите продолжить? (Y/N) ').upper()
            if is_continue == 'Y':
                return True
            elif is_continue == 'N':
                return False
            else:
                print('Ошибка ввода!')


first_player_name = input('Введите имя первого игрока: ')
second_player_name = input('Введите имя второго игрока: ')
player_1 = Player(first_player_name, 'x')
player_2 = Player(second_player_name, 'o')
while True:
    game = Game(player_1, player_2)
    game.board.board_state()
    if game.start_game():
        continue
    else:
        break

# можно укоротить
# if not game.start_game():
#   break
