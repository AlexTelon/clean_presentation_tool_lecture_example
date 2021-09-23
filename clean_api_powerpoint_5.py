import os
import math
def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self):
        self.slides = ['1. Hello', '2. Heading', '3. Stuff', '4. Questions?']
        # Renamed _i to _page
        self._page = 1
        self._n = len(self.slides)

    @property
    def current(self):
        # page starts at 1, while list indexing start at 0.
        return self.slides[self._page - 1]

    # Renamed index -> page
    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        # Clamp the value to within the available pages.
        self._page = min(self._n, max(1, value))

    def left(self):
        self.page -= 1

    def right(self):
        self.page += 1

    def home(self):
        # page 1 is now homepage.
        self.page = 1

    def end(self):
        self.page += math.inf


slides = Slides()
prev_c = 'home'
while True:
    c = input('')

    # Enter repeats the previuos typed command.
    if c == '':
        c = prev_c

    if c.isdigit():
        slides.index = int(c)
    elif c in ['right', 'r']:
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