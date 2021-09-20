import os
import math
def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self):
        # We could also make pages into a 1-indexed collection by injecting a dummy page at the beginning.
        # Not saying this is better, but it is another option.
        self.pages = ['', '1. Hello', '2. Heading', '3. Stuff', '4. Questions?']
        self._page = 1
        self._n = len(self.pages)

    @property
    def current(self):
        # page starts at 1, while list indexing start at 0.
        return self.pages[self._page]

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        # Clamp the value to within the available pages.
        self._page = min(self._n-1, max(1, value))


slides = Slides()

prev_c = 'home'
while True:
    c = input('')

    # Enter repeats the previuos typed command.
    if c == '':
        c = prev_c

    if c.isdigit():
        slides.page = int(c)
    elif c in ['right', 'r']:
        slides.page += 1
    elif c in ['left', 'l']:
        slides.page -= 1
    elif c in ['home', 'h']:
        slides.page = 1
    elif c in ['end', 'e']:
        slides.page = math.inf
    elif c in ['quit', 'q']:
        exit()

    # clear screen
    cls()

    # Draw new content
    print(slides.current)

    prev_c = c