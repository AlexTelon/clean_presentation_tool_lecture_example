import math

from cls import cls


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
        self._page = min(self._n-1, max(1, value))


# Now we intialize the slides, such that we can create different types of slides.
# Before it was hardcoded inside the Slides constructor.
slides = Slides(['1. Hello', '2. Heading', '3. Stuff', '4. Questions?'])

# Improved the default value.
# The default should be to go right, right? Now pressing enter goes right.
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