import os

class TicTacToeGame:
    def __init__(self):
        self.board_size = 3
        self.current_player = 'X'
        self.board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.scores = {'X': 0, 'O': 0}
        self.move_history = []

    def display_board(self):
        os.system('clear')  # Clear the terminal (works on Linux/macOS)
        print("Tic-Tac-Toe")
        for row in self.board:
            print("|".join(row))
            print("-" * (self.board_size * 2 - 1))
        print(f"Player X Score: {self.scores['X']}, Player O Score: {self.scores['O']}\n")

    def get_player_move(self):
        while True:
            move = input(f"Player {self.current_player}, enter your move (e.g., A1): ").strip().upper()
            if len(move) != 2 or move[0] not in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'[:self.board_size] or move[1] not in '123456789'[:self.board_size]:
                print("Invalid move. Please enter a valid move.")
            else:
                return move

    def make_move(self, move):
        row, col = ord(move[0]) - ord('A'), int(move[1]) - 1
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            self.move_history.append((row, col))
            return True
        else:
            return False

    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(self.board_size):
            if all(self.board[i][j] == self.current_player for j in range(self.board_size)) or \
               all(self.board[j][i] == self.current_player for j in range(self.board_size)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(self.board_size)) or \
           all(self.board[i][self.board_size - 1 - i] == self.current_player for i in range(self.board_size)):
            return True
        return False

    def undo_move(self):
        if self.move_history:
            row, col = self.move_history.pop()
            self.board[row][col] = ' '
            self.current_player = 'X' if self.current_player == 'O' else 'O'

    def redo_move(self):
        if self.move_history:
            row, col = self.move_history[-1]
            if self.board[row][col] == ' ':
                self.current_player = 'X' if self.current_player == 'O' else 'O'
                self.board[row][col] = self.current_player

    def update_scores(self):
        if self.check_winner():
            self.scores[self.current_player] += 1

    def play(self):
        while True:
            self.display_board()
            move = self.get_player_move()
            if move == 'QUIT':
                break
            if move == 'UNDO':
                self.undo_move()
            elif move == 'REDO':
                self.redo_move()
            else:
                if self.make_move(move):
                    if self.check_winner():
                        self.display_board()
                        print(f"Player {self.current_player} wins!")
                        self.update_scores()
                        self.display_board()
                        play_again = input("Play again? (yes/no): ").strip().lower()
                        if play_again != 'yes':
                            break
                    else:
                        self.current_player = 'X' if self.current_player == 'O' else 'O'
                else:
                    print("Invalid move. The cell is already occupied.")

def main():
    game = TicTacToeGame()
    game.play()

if __name__ == "__main__":
    main()
