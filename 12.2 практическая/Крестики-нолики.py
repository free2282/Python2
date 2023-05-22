import random
from abc import ABC, abstractmethod


# Класс, отражающий сущность клетки игры (содержит свой номер - __number, булево значение занята она или нет - __taken,
# булево значение, каким игроком она занята - __taken_by_first_player)
class Cell:

    # Метод инициализации клетки игрового поля
    def __init__(self, taken=False, taken_by_first_player=False, number: int = 0):
        self.__taken = taken
        self.__taken_by_first_player = taken_by_first_player
        self.__number = number

    # Метод получения статуса занятия клетки
    def is_taken(self):
        return self.__taken

    # Метод получения статуса занятия клетки первым игроков
    def is_taken_by_first_player(self):
        return self.__taken_by_first_player

    # Метод получения номера клетки
    def get_number(self):
        return self.__number

    # Метод занятия клетки
    def take_cell(self, taken_by_first_player):
        self.__taken = True
        self.__taken_by_first_player = taken_by_first_player


# Класс, отражающий сущность доски (содержит в себе список клеток на доске - __cells, представленных классом Cell)
class Board:

    # Метод инициализации обЪекта доски
    def __init__(self):
        self.__cells = list()
        for i in range(1, 10):
            self.__cells.append(Cell(number=i))

    # Метод печати игрового поля
    def print_board(self):
        self.__print_game_row(list(range(1, 4)))
        print("-+-+-")

        self.__print_game_row(list(range(4, 7)))
        print("-+-+-")

        self.__print_game_row(list(range(7, 10)))

    # Метод получения статуса занятия клетки
    def is_cell_taken(self, index: int):
        return self.__get_cell(index).is_taken()

    # Метод занятия клетки
    def take_cell(self, index: int, taken_by_first_player: bool):
        self.__get_cell(index).take_cell(taken_by_first_player)

    # Метод проверки победы одного из игроков на поле
    def check_if_win(self, is_first_player: bool) -> bool:
        if self.__check_three_in_row([1, 2, 3], is_first_player):
            return True
        if self.__check_three_in_row([1, 4, 7], is_first_player):
            return True
        if self.__check_three_in_row([1, 5, 9], is_first_player):
            return True
        if self.__check_three_in_row([4, 5, 6], is_first_player):
            return True
        if self.__check_three_in_row([7, 8, 9], is_first_player):
            return True
        if self.__check_three_in_row([2, 5, 8], is_first_player):
            return True
        if self.__check_three_in_row([3, 6, 9], is_first_player):
            return True
        if self.__check_three_in_row([3, 5, 7], is_first_player):
            return True
        return False

    # Метод определения "трёх в ряд"
    def __check_three_in_row(self, indexes: list[int], is_first_player: bool) -> bool:
        for index in indexes:
            if (not self.__get_cell(index).is_taken_by_first_player() == is_first_player) or not self.is_cell_taken(
                    index):
                return False
        return True

    # Метод получения клетки по номеру
    def __get_cell(self, index: int) -> Cell:
        return next(filter(lambda cell: cell.get_number() == index, self.__cells))

    # Метод для печати строки игрового поля
    def __print_game_row(self, indexes: list):
        print(self.__get_symbol_to_print(self.__get_cell(indexes[0])), end="|")
        print(self.__get_symbol_to_print(self.__get_cell(indexes[1])), end="|")
        print(self.__get_symbol_to_print(self.__get_cell(indexes[2])), end=f" {indexes[0]} {indexes[1]} {indexes[2]}\n")

    # Метод получения символа для печати в клетке
    def __get_symbol_to_print(self, cell: Cell) -> str:
        if cell.is_taken() and cell.is_taken_by_first_player():
            return "X"
        elif cell.is_taken() and not cell.is_taken_by_first_player():
            return "O"
        else:
            return " "


# Класс, отражающий сущность игрока (содержит булево значение выиграл игрок или нет - __won, имя игрока - __player_name)
class Player(ABC):

    # Метод инициализации игрока
    def __init__(self, won=False, player_name="X"):
        self.__won = won
        self.__player_name = player_name

    # Метод получения статуса победы игрока
    def is_won(self) -> bool:
        return self.__won

    # Метод пометки игрока, как выигравшего
    def make_won(self):
        self.__won = True

    # Метод получения имени игрока
    def get_player_name(self):
        return self.__player_name

    # Абстрактный метод получения клетки, которую займет игрок. Наследники должны реализовать
    @abstractmethod
    def input_cell_number(self):
        pass


# Класс, отражающий сущность игрока-человека
class HumanPlayer(Player):

    # Метод, отвечающий за получение значения клетки для игрока-человека
    def input_cell_number(self) -> int:
        cell_number = input()

        while not cell_number.isdigit():
            print("Incorrect Value! Try Again!")
            cell_number = input("")
        return int(cell_number)


# Класс, отражающий сущность игрока-компьютера
class PcPlayer(Player):

    # Метод, отвечающий за получение случайного значения клетки для игрока-компьютера
    def input_cell_number(self):
        cell_number = random.randint(1, 9)
        return cell_number


# Класс, отражающий сущность игровой механики
class Game:

    # Метод, отвечащий за инициализацию объекта игры
    def __init__(self, first_player_turn=True):
        self.first_player_turn = first_player_turn

    # Метод, отвечающий за попытку занять клетку. Возвращает false, если клетку нельзя занять
    def try_take_cell(self, game_board: Board, index: int, taken_by_first_player: bool) -> bool:
        if not game_board.is_cell_taken(index):
            game_board.take_cell(index, taken_by_first_player)
            return True
        return False

    # Метод, отвечающий за проверку победил игрок или нет
    def make_won_if_player_win(self, player: Player, first_player_turn: bool, game_board: Board):
        if game_board.check_if_win(first_player_turn):
            player.make_won()

    # Метод, отражающий логику хода игрока
    def player_turn(self, player: Player, game_board: Board, first_player_turn: bool):
        print(f"What is {player.get_player_name()}'s move? (1-9)")
        cell_number = player.input_cell_number()
        while not self.try_take_cell(game_board, int(cell_number), first_player_turn):
            if isinstance(player, HumanPlayer):
                print("This cell already taken! Choose another!")
            cell_number = player.input_cell_number()
        if isinstance(player, PcPlayer):
            print(cell_number)
        game_board.print_board()
        self.make_won_if_player_win(player, first_player_turn, game_board)

    # Главный метод игры, отвечающий за игровой процесс
    def main(self):
        player_choice = input(
            "Do you want to play with computer or by rotation? (1 - with computer, 2 - by rotation): ")

        while not player_choice.isdigit():
            print("Incorrect Value! Try Again!")
            player_choice = input(
                "Do you want to play with computer or by rotation? (1 - with computer, 2 - by rotation): ")

        with_pc = True if int(player_choice) == 1 else False

        if with_pc:
            player_x = HumanPlayer(player_name="X")
            player_o = PcPlayer(player_name="O")
        else:
            player_x = HumanPlayer(player_name="X")
            player_o = HumanPlayer(player_name="O")

        game_board = Board()

        counter = 9

        print("Welcome to tic-tac-toe!")
        game_board.print_board()

        while (not player_x.is_won()) and (not player_o.is_won()) and (counter > 0):
            if self.first_player_turn:
                self.player_turn(player_x, game_board, self.first_player_turn)
            else:
                self.player_turn(player_o, game_board, self.first_player_turn)

            self.first_player_turn = not self.first_player_turn
            counter = counter - 1

        if player_x.is_won():
            print(f"{player_x.get_player_name()} has won the game!")
        elif player_o.is_won():
            print(f"{player_o.get_player_name()} has won the game!")
        else:
            print("Game tied!")

        print("Thanks for playing!")


Game().main()