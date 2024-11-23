# Triditional X/O chess game in a # board.
# class Board, class Player, class Game are defined.

# class Board will have print func and
class Board:
    def __init__(self) -> None:
        self.board = [' '] * 9

    def print_board(self):
        print("\n")
        print(" ", self.board[0], "|", self.board[1], "|", self.board[2])
        print("-------------")
        print(" ", self.board[3], "|", self.board[4], "|", self.board[5])
        print("-------------")        
        print(" ", self.board[6], "|", self.board[7], "|", self.board[8])

    def update_board(self, position, mark):
        try:
            if self.board[position - 1] == " ":
                self.board[position - 1] = mark
                return True
            else:
                print("This position is used, please choose another space:")
                return False
        except:
            print("invalid position, please enter 1-9")

    def check_winner(self, mark):
        if (self.board[0] == mark and self.board[1] == mark and self.board[2] == mark) or \
           (self.board[3] == mark and self.board[4] == mark and self.board[5] == mark) or \
           (self.board[6] == mark and self.board[7] == mark and self.board[8] == mark) or \
           (self.board[0] == mark and self.board[3] == mark and self.board[6] == mark) or \
           (self.board[1] == mark and self.board[4] == mark and self.board[7] == mark) or \
           (self.board[2] == mark and self.board[5] == mark and self.board[8] == mark) or \
           (self.board[0] == mark and self.board[4] == mark and self.board[8] == mark) or \
           (self.board[2] == mark and self.board[4] == mark and self.board[6] == mark):
            return True
        else:
            return False

    def check_draw(self):
        if " " not in self.board:
            return True
        else:
            return False

class Player:
    def __init__(self, mark) -> None:
        self.mark = mark
        self.name = self.get_name()

    def get_name(self):
        if self.mark == "X":
            name = input("X player, please enter your name: ")
        else:
            name = input("O player, please enter your name: ")
        return name
        
class Game:
    def __init__(self) -> None:
        self.board = Board()
        self.player1 = Player("X")
        self.player2 = Player("O")
        self.current_player = self.player1

    def play(self):
        while True:
            try:
                #ask current player to select a free space to mark it.
                message = f"Player {self.current_player.name} please enter (1-9): "
                position = int(input(message))
                #use self.board.update_board() to check if update success
                #If yes, switch to another player to move forward.
                if self.board.update_board(position, self.current_player.mark):
                    self.board.print_board()
                    # check if someone wins or draw, end the game when it is true.
                    if self.board.check_winner(self.current_player.mark):
                        print(f"{self.current_player.name} wins the game.")
                        break
                    elif self.board.check_draw():
                        print("Game is end with draw!")
                        break
                    if self.current_player == self.player1:
                        self.current_player = self.player2
                    else:
                        self.current_player = self.player1
            except:
                print("Please enter 1-9!")



game = Game()
game.play()