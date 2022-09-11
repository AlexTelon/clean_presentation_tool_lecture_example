import math

from cls import cls

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
        # Before left/right had to keep sure we did not get out of bounds.
        self.index -= 1

    def right(self):
        # Before left/right had to keep sure we did not get out of bounds.
        self.index += 1

    def home(self):
        self.index = 0

    def end(self):
        self.index += math.inf


slides = Slides()
prev_c = 'home'
while True:
    c = input('')

    # Enter repeats the previuos typed command.
    if c == '':
        c = prev_c

    if c in ['right', 'r']:
        slides.right()
    elif c in ['left', 'l']:
        slides.left()
    elif c in ['home', 'h']:
        slides.home()
    elif c in ['end', 'e']:
        slides.end()
    elif c in ['quit', 'q']:
        exit()


    # clear screen
    cls()

    # Draw new content
    print(slides.current)

    prev_c = c