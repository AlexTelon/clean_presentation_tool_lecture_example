import os
def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self):
        self.slides = ['1. Hello', '2. Heading', '3. Stuff', '4. Questions?']
        self.index = 0

    def current_slide(self):
        return self.slides[self.index]

    def left(self):
        self.index -= 1

    def right(self):
        self.index += 1

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
    print(slides.current_slide())

    prev_c = c