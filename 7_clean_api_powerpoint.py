import os
import math
def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self, slides):
        # Add dummy slide at start to 0-index the slides
        self.slides = [""] + slides
        self._page = 1
        self._n = len(self.slides)

    @property
    def current(self):
        return self.slides[self._page]

    @property
    def page(self):
        return self._page

    @page.setter
    def page(self, value):
        # Clamp the value to within the available pages.
        self._page = min(self._n-1, max(1, value))


# Slides should be initializable, not hardcoded ofc.
slides = Slides(['1. Hello', '2. Heading', '3. Stuff', '4. Questions?'])

# The default should be to go right, right?
prev_c = 'right'
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