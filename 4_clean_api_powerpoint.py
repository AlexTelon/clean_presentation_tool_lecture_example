import os
import math
def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self):
        self.slides = ['1. Hello', '2. Heading', '3. Stuff', '4. Questions?']
        self._i = 0
        self._n = len(self.slides)

    @property
    def current(self):
        return self.slides[self.index]

    # Added getter and setter for index.
    @property
    def index(self):
        return self._i

    # The setter for index now deals with the index
    @index.setter
    def index(self, value):
        # Clamp the value to within the available slides.
        self._i = min(self._n-1, max(0, value))

    def left(self):
        self.index -= 1

    def right(self):
        self.index += 1

    def home(self):
        self.index = 0

    def end(self):
        self.index += math.inf


slides = Slides()
commands = {
    'left':     slides.left,
    'right':    slides.right,
    'home':     slides.home,
    'end':      slides.end,
    'quit':     lambda: exit(),
    'q':        lambda: exit(),
}

prev_c = 'home'
while True:
    c = input('')

    # Enter repeats the previuos typed command.
    if c == '':
        c = prev_c

    # Lets add the ability to use number to jump!
    if c.isdigit():
        # It works, but it feels wonky with 0 indexing for slides.
        # So we add -1 here.
        slides.index = int(c) - 1
    else:
        # Get the command. Or do nothing if you dont recognize it.
        commands[c]()

    # clear screen
    cls()

    # Draw new content
    print(slides.current)

    prev_c = c