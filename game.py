from Tic_tac_toe.board import Board


class Game:
    def __init__(self, player='x') -> None:
        self.board = Board()
        self.player = player
        self.cordinate_win = (
                (1, 2, 3), (4, 5, 6), (7, 8, 9),
                (1, 4, 7), (2, 5, 8), (3, 6, 9),
                (1, 5, 9), (3, 5, 7))

    def input_value(self) -> bool:
        try:
            cord = int(input(f'Ход игрока {self.player}. Введите номер клетки (1-9):').strip())

        except ValueError:
            print('Введите корректное число от 1 до 9.')
            return False
        
        if not 1 <= cord <= 9:
            print(f'Клетки {cord} не существует')
            return False
        
        if self.board.board[cord] is None:
            self.board.board[cord] = self.player
            return True

        else:
            print(f'Клетка {cord} - уже занята')
            print()
            return False

    def check_win(self) -> bool:
        for win_cord in self.cordinate_win:
            values = [self.board.board[cord] for cord in win_cord]
            if len(set(values)) == 1 and values[0] is not None:
                return True
        return False

    def switch_player(self) -> str:
        self.player = 'o' if self.player == 'x' else 'x'