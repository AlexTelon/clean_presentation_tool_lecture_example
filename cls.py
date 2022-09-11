import os

# Ensure that we have a way to clear the terminal screen
# Windows and linux style systems do it differently.
# Windows: cls, Linux: clear.
# However git-bash on windows uses linux style commands for instance.
# So instead of checking which OS we are on we simply try clear commands until we
# find one that does not return an error code!
for command in ['clear', 'cls']:
    if os.system(command) == 0:
        cls = lambda: os.system(command)
        break