from cls import cls


class Slides():
    def __init__(self):
        self.slides = ['1. Hello', '2. Heading', '3. Stuff', '4. Questions?']
        self.index = 0

    # Made this into a property, renamed to just current. The '_slide' part was unecessary.
    @property
    def current(self):
        return self.slides[self.index]

    def left(self):
        # Now stopping at the edge.
        self.index = max(0, self.index - 1)

    def right(self):
        # Now stopping at the edge.
        self.index = min(len(self.slides) - 1, self.index+1)

    def home(self):
        self.index = 0

    def end(self):
        self.index = len(self.slides) - 1


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