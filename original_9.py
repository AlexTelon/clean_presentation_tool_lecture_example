import os
import math
import sys
from typing import Iterable


def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self, slides: Iterable[str]):
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


def load_slides(filename):
    slides = []
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    slide = []
    # Sentinel # list item at to ensure the last item is added too.
    for line in lines + ['#']:
        if line.startswith('#'):
            slides.append("\n".join(slide))
            slide = []
        slide.append(line)

    return slides


if __name__ == "__main__":
    # Load the presentation!
    load_file = 'sample_slides_9.txt'
    if len(sys.argv) > 1:
        load_file = sys.argv[1]

    content = load_slides(load_file)
    slides = Slides(content)

    # Start the presentation.
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