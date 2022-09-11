import math
import sys
from typing import Iterable

from cls import cls


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
        self._page = min(self._n-1, max(1, value))

# Added a new load_slides function
def load_slides(filename):
    slides = []
    with open(filename, 'r') as f:
        lines = f.read().splitlines()

    slide = []
    # Sentinel # list item at end to ensure the last item is added too.
    for line in lines + ['#']:
        if line.startswith('#'):
            # If the first line is a heading (as it should) we hit
            # this directly and we are not interested in adding an empty slide here.
            if any(slide):
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
    cls()
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