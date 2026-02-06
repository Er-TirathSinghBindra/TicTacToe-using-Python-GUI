'''
Game Logic Engine for TicTacToe
'''
import numpy as np
import random
from constants import PLAYERS, VALUE_X, VALUE_O

class TicTacToeEngine:
    def __init__(self):
        self.reset()

    def reset(self):
        # Board Status (empty strings)
        self.board_status = np.array([
            ['', '', ''],
            ['', '', ''],
            ['', '', '']
        ])
        
        # Board Scores (+1 for X, -1 for O)
        self.board_score = np.array([
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0]
        ])

        # Choosing start player randomly
        self.curr_player = random.choice(PLAYERS)
        self.player_index = PLAYERS.index(self.curr_player)
        
        self.board_size = 3
        self.remaining_moves = self.board_size ** 2
        self.game_won = False
        self.game_over = False

        # For main algorithm matrix multiplication
        self.mul_mat = np.array([1] * self.board_size).reshape(self.board_size, 1)

    def is_available(self, row, col):
        return self.board_status[row][col] == ''

    def make_move(self, row, col):
        if self.game_won or self.game_over:
            return False, "Game is already over"

        if not self.is_available(row, col):
            return False, "Position already occupied"

        # Update board status and score
        self.board_status[row][col] = self.curr_player
        self.board_score[row][col] = VALUE_X if self.curr_player == 'X' else VALUE_O
        self.remaining_moves -= 1

        # Check for win
        self.game_won = self.has_won()
        
        if self.game_won:
            return True, f"{self.curr_player} has WON!!!"

        if self.remaining_moves == 0:
            self.game_over = True
            return True, "No moves left!!!"

        # Switch player
        self.next_player()
        return True, f"Player {self.curr_player}'s turn"

    def next_player(self):
        self.player_index = (self.player_index + 1) % len(PLAYERS)
        self.curr_player = PLAYERS[self.player_index]

    def has_won(self):
        sum_rows = self.board_score.dot(self.mul_mat).T.tolist()[0]
        sum_cols = self.mul_mat.T.dot(self.board_score).tolist()[0]
        sum_diag = np.trace(self.board_score)
        sum_anti_diag = np.trace(np.flipud(self.board_score))

        # Check if X won (3) or O won (-3)
        target = 3 if self.curr_player == 'X' else -3
        
        if (target in sum_rows) or (target in sum_cols) or (sum_diag == target) or (sum_anti_diag == target):
            return True
            
        return False
