class Board:
    def __init__(self) -> None:
        self.board = dict.fromkeys([i for i in range(1, 10)], None)

    def print_board(self):
        print()
        for horizontally in range(3):
            for vertical in range(3):
                key = 3 * horizontally + vertical + 1
                value = self.board[key] if self.board[key] is not None else ' '

                if vertical != 2:
                    print(f' {value} |', end='')
                else:
                    print(f' {value} ', end='')

            if horizontally != 2:
                print('\n ---------')
        print()
        print()

    def is_full(self):
        return all(value is not None for value in self.board.values())