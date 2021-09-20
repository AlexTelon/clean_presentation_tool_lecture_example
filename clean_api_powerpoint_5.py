import os
import math
def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self):
        self.slides = ['1. Hello', '2. Heading', '3. Stuff', '4. Questions?']
        self._page = 1
        self._n = len(self.slides)

    @property
    def current(self):
        # page starts at 1, while list indexing start at 0.
        return self.slides[self._page - 1]

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

    if c.isdigit():
        slides.page = int(c)
    else:
        # Get the command. Or do nothing if you dont recognize it.
        commands[c]()

    # clear screen
    cls()

    # Draw new content
    print(slides.current)

    prev_c = c