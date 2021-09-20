import os
import math
import sys
from typing import Iterable


def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)

# Create a new Slide class.
# With this we can implement a feature to show/hide parts of a slide during a presentation
class Slide():
    """Represents a slide in a presentation."""
    def __init__(self, content: str):
        self._content_lines = content.splitlines()
        self._n = len(self._content_lines)

        # How many rows to show. Default to all
        self.row = math.inf

    @property
    def row(self):
        """How many rows of this slide to show."""
        return self._row

    @row.setter
    def row(self, value):
        # Always show at least the heading (first row)!
        value = max(1, value)
        # Never try to show more than all rows.
        self._row = min(self._n, value)

    def __str__(self):
        return "\n".join(self._content_lines[:self._row])

    def __repr__(self):
        # If you inspect slides while debugging then this is what you will see.
        return f'Slide([{",".join(self._content_lines[:self._row])}])'


class Slides():
    """Represents a deck of slides for a presentation."""
    def __init__(self, slides: Iterable[str]):
        # Add dummy slide at start to 0-index the slides
        self._slides = [Slide("")] + [Slide(content) for content in slides]
        self._page = 1
        self._n = len(self._slides)

    @property
    def current(self):
        return self._slides[self._page]

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
        # Added two new command
        # down and up let you control how much is shown on the current slide!
        elif c in ['down', 'd']:
            slides.current.row += 1
        elif c in ['up', 'u']:
            slides.current.row -= 1
        elif c in ['quit', 'q']:
            exit()

        # clear screen
        cls()

        # Draw new content
        print(slides.current)

        prev_c = c