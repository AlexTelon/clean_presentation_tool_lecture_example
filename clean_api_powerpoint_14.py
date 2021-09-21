import math
import os
import shelve
import sys
from typing import Iterable

def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)

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
        return f'Slide([{",".join(self._content_lines[:self._row])}])'


class Slides():
    """Represents a deck of slides for a presentation."""
    def __init__(self, slides: Iterable[str]):
        # Ensure that the _slides are 1-indexed by ensuring the precense of an empty dummy slide at position 0.
        self._slides = (Slide(""),) + tuple(Slide(content) for content in slides)
        self._page = 1
        self._n = len(self._slides)

    @classmethod
    def from_file(cls, filename: str):
        """Creates Slides from a file."""
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

        # Now call __init__ with the content for each slide.
        # Skip the first empty slide however
        # NOTE: I am tempted to leave it here (since we want a dummy empty one anyways)
        #       But that feels more like a hack. Besides __init__ still needs to inject 
        #       an empty slide if the user calls __init__ directly which would lead to
        #       extra logic.
        return cls(slides[1:])

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


class Database():
    """Database abstraction. Provides a persistant key-value store for Slides objects."""
    def __init__(self):
        # Outside of Database we dont need to care if we change the database implementation.
        self._d = shelve.open('.slides_db')
    
    def store_slides(self, slides: Slides, key: str) -> None:
        self._d[key] = slides

    def get_slides(self, key: str) -> Slides:
        return self._d[key]
    
    def has_slides(self, key: str) -> bool:
        return key in self._d

def render_page(content: str):
    """Takes an markdown-like string and transforms to html."""
    lines = []
    lines.append(' <meta http-equiv="refresh" content="1" />')

    is_heading = lambda line: line.startswith('#')

    for line in content.splitlines():
        if is_heading(line):
            line = f"<h1>{line.replace('# ', '').replace('#', '')}</h1>"
        else:
            line = f"<p>{line}</p>"
        lines.append(line)

    return "\n".join(lines)


if __name__ == "__main__":
    load_file = 'sample_slides_9.txt'
    if len(sys.argv) > 1:
        load_file = sys.argv[1]

    # Create our new database object
    db = Database()

    # Load the presentation!
    if db.has_slides(load_file):
        slides = db.get_slides(load_file)
    else:
        slides = Slides.from_file(load_file)


    # Start the presentation.
    prev_c = 'right'
    while True:
        # clear screen
        cls()

        # Draw slide to cli.
        print(slides.current)

        # Draw slide to auto-refreshing webpage in browser.
        with open('index.html', 'w') as f:
            html_content = render_page(str(slides.current))
            f.write(html_content)

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
        elif c in ['down', 'd']:
            slides.current.row += 1
        elif c in ['up', 'u']:
            slides.current.row -= 1
        elif c in ['quit', 'q']:
            # Before quiting we now store the slides to our db.
            db.store_slides(slides, load_file)
            exit()

        prev_c = c