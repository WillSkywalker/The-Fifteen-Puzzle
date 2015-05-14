"""
GUI for the Fifteen puzzle
"""

from Tkinter import *

# constants
TILE_SIZE = 80
KEY_MAP = {'up':8320768,
           'down':8255233,
           'left':8124162,
           'right':8189699,
}


class FifteenGUI:
    """
    Main GUI class
    """

    def __init__(self, puzzle):
        """
        Create frame and timers, register event handlers
        """
        self._puzzle = puzzle
        self._puzzle_height = puzzle.get_height()
        self._puzzle_width = puzzle.get_width()
        self._root = Tk()
        self._root.title("Fifteen Puzzle")
        self._frame = Canvas(self._root, bg='#FFFFFF',
                             width=self._puzzle_width * TILE_SIZE,
                             height=self._puzzle_height * TILE_SIZE)
        self._frame.grid(columnspan=4)
        self._solution = ""
        self._current_moves = ""

        Button(self._root, text='Solve', command=self.solve).grid(row=1, column=0)
        Button(self._root, text='Print moves', 
               command=self.print_moves).grid(row=1, column=3)

        self.input_move = Entry(self._root)
        self.input_move.bind("<Return>", self.enter_moves)
        self.input_move.grid(row=1, column=1)

        self._root.bind(sequence='<KeyPress-Up>', func=self.keydown)
        self._root.bind(sequence='<KeyPress-Down>', func=self.keydown)
        self._root.bind(sequence='<KeyPress-Left>', func=self.keydown)
        self._root.bind(sequence='<KeyPress-Right>', func=self.keydown)
        self._root.after(250, self.tick)

        self.draw(self._frame)
        self._root.mainloop()

    def tick(self):
        """
        Timer for incrementally displaying computed solution
        """
        if self._solution == "":
            self._root.after(250, self.tick)
            return
        direction = self._solution[0]
        self._solution = self._solution[1:]
        try:
            self._puzzle.update_puzzle(direction)
        except:
            print "invalid move:", direction
        self.draw(self._frame)
        self._root.after(250, self.tick)

    def solve(self):
        """
        Event handler to generate solution string for given configuration
        """
        new_puzzle = self._puzzle.clone()
        self._solution = new_puzzle.solve_puzzle()
        self.draw(self._frame)

    def print_moves(self):
        """
        Event handler to print and reset current move string
        """
        print self._current_moves
        self._current_moves = ""

    def enter_moves(self, event):
        """
        Event handler to enter move string
        """
        self._solution = self.input_move.get()

    def keydown(self, key):
        """
        Keydown handler that allows updates of puzzle using arrow keys
        """
        if key.keycode == KEY_MAP["up"]:
            try:
                self._puzzle.update_puzzle("u")
                self._current_moves += "u"
            except:
                print "invalid move: up"
        elif key.keycode == KEY_MAP["down"]:
            try:
                self._puzzle.update_puzzle("d")
                self._current_moves += "d"
            except:
                print "invalid move: down"
        elif key.keycode == KEY_MAP["left"]:
            try:
                self._puzzle.update_puzzle("l")
                self._current_moves += "l"
            except:
                print "invalid move: left"
        elif key.keycode == KEY_MAP["right"]:
            try:
                self._puzzle.update_puzzle("r")
                self._current_moves += "r"
            except:
                print "invalid move: right"
        self.draw(self._frame)

    def draw(self, canvas):
        """
        Draw the puzzle
        """
        canvas.delete()
        for row in range(self._puzzle_height):
            for col in range(self._puzzle_width):
                tile_num = self._puzzle.get_number(row, col)
                if tile_num == 0:
                    background = "#8080FF"
                else:
                    background = "blue"
                tile = ([col * TILE_SIZE, row * TILE_SIZE],
                        [(col + 1) * TILE_SIZE, row * TILE_SIZE],
                        [(col + 1) * TILE_SIZE, (row + 1) * TILE_SIZE],
                        [col * TILE_SIZE, (row + 1) * TILE_SIZE])
                canvas.create_polygon(*tile, outline="white", fill=background)
                canvas.create_text((col + .2) * TILE_SIZE,
                                (row + 0.8) * TILE_SIZE,
                                text=str(tile_num), fill="white")



