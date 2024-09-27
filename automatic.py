from Tic_tac_toe.game import Game


class Automatic(Game):
    def __init__(self, player='x') -> None:
        super().__init__(player)
        self.game = Game()
        
    def game_start(self):
        
        self.game.board.print_board()
        while True:
            if self.game.board.is_full():
                print('Ничья!')
                break

            if not self.game.input_value():
                continue

            if self.game.check_win():
                self.game.board.print_board()
                print(f'Игрок {self.game.player} победил!')
                break
            
            self.game.switch_player()
            self.game.board.print_board()