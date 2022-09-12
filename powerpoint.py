from cls import cls


class Slides():
    def __init__(self):
        self.slides = ['1. Hello', '2. Heading\n\nderp', '3. Stuff', '4. Questions?']
        self.index = 0

    def current_slide(self):
        return self.slides[self.index]

    def left(self):
        self.index = max(0,  self.index - 1)

    def right(self):
        self.index = min(len(self.slides) - 1,  self.index + 1)

    def home(self):
        self.index = 0

    def end(self):
        self.index = len(self.slides) - 1


slides = Slides()
prev_c = 'home'
while True:
    # clear screen
    cls()

    # Draw new content
    print(slides.current_slide())

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

    prev_c = c