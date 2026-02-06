'''
Graphical User Interface for TicTacToe
'''
import tkinter as tk
from tkinter import StringVar
from constants import DEFAULT_WIDTH, DEFAULT_HEIGHT, LINE_WIDTH, CHAR_WIDTH

class TicTacToeGUI:
    def __init__(self, engine, width=DEFAULT_WIDTH, height=DEFAULT_HEIGHT):
        self.engine = engine
        self.width = width
        self.height = height
        
        # Creating root Window
        self.root = tk.Tk()
        self.root.title("TicTacToe")
        self.root.resizable(width=False, height=False)

        # Label Text Variable
        self.info_text = StringVar()

        # Creating canvas
        self.create_canvas()
        # Creating board on canvas
        self.create_board()
        
        # Initial message
        self.info_text.set(f"Player {self.engine.curr_player} start")

    def create_canvas(self):
        self.main_canvas = tk.Canvas(self.root, width=self.width, height=self.height)
        # Adding button press event to main canvas
        self.main_canvas.bind("<ButtonPress-1>", self.handle_click)
        # To pack the canvas on root window
        self.main_canvas.pack()
        self.info_label = tk.Label(self.root, bg='#87ceeb', textvariable=self.info_text)
        self.info_label.pack(fill=tk.X)

    def create_board(self):
        # Creating Vertical Lines
        self.main_canvas.create_line(self.width/3, 0, self.width/3, self.height, width=LINE_WIDTH)
        self.main_canvas.create_line(2*self.width/3, 0, 2*self.width/3, self.height, width=LINE_WIDTH)

        # Creating Horizontal Lines
        self.main_canvas.create_line(0, self.height/3, self.width, self.height/3, width=LINE_WIDTH)
        self.main_canvas.create_line(0, 2*self.height/3, self.width, 2*self.height/3, width=LINE_WIDTH)

    def draw_character(self, data, row, col):
        height_offset = 0.1 * self.height
        width_offset = 0.1 * self.width

        # Determining x,y coordinates
        x1 = col * self.width/3 + width_offset
        y1 = row * self.height/3 + height_offset
        x2 = (col + 1) * self.width/3 - width_offset
        y2 = (row + 1) * self.height/3 - height_offset

        if data == 'O':
            self.main_canvas.create_oval(x1, y1, x2, y2, width=CHAR_WIDTH)
        elif data == 'X':
            self.main_canvas.create_line(x1, y1, x2, y2, width=CHAR_WIDTH)
            self.main_canvas.create_line(x1, y2, x2, y1, width=CHAR_WIDTH)

    def handle_click(self, event):
        if self.engine.game_won or self.engine.game_over:
            self.info_text.set('Game Over!!! Click Here To Reset!!!')
            self.info_label.bind('<Button-1>', self.reset_game)
            return

        # Converting click location to array index
        row = int(event.y // (self.height/3))
        col = int(event.x // (self.width/3))
        
        # Constraints to 0-2 (in case of weird clicks on edges)
        row = max(0, min(2, row))
        col = max(0, min(2, col))

        # Check if engine accepts the move
        if self.engine.is_available(row, col):
            player = self.engine.curr_player
            success, message = self.engine.make_move(row, col)
            if success:
                self.draw_character(player, row, col)
                self.info_text.set(message)
                
                if self.engine.game_won or self.engine.game_over:
                    self.info_label.bind('<Button-1>', self.reset_game)
        else:
            self.info_text.set('Position already occupied')

    def reset_game(self, event=None):
        self.engine.reset()
        self.main_canvas.delete('all')
        self.create_board()
        self.info_text.set(f"Player {self.engine.curr_player} start")
        self.info_label.unbind('<Button-1>')

    def run(self):
        self.root.mainloop()
