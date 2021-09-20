import os
def cls():
    """Clears the terminal screen"""
    # os.system('cls') # windows
    os.system('clear') # linux (or git-bash for windows)


class Slides():
    def __init__(self):
        self.slides = ['1. Hello', '2. Heading', '3. Stuff', '4. Questions?']
        self.index = 0

    @property
    def current(self):
        return self.slides[self.index]

    def left(self):
        # self.index -= 1
        self.index = max(0, self.index-1)

    def right(self):
        self.index = min(len(self.slides)-1, self.index+1)
        # self.index += 1

    def home(self):
        self.index = 0

    def end(self):
        self.index = len(self.slides) - 1

slides = Slides()

commands = {
    'left': slides.left,
    'right': slides.right,
    'home': slides.home,
    'end': slides.end,
    'quit': lambda: exit(),
    'q': lambda: exit(),
}


while True:
    c = input('')

    commands[c]()

    # clear screen
    cls()

    # Draw new content
    print(slides.current)