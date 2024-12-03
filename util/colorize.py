from util.special_chars import special_chars

def colorize(color, message = ''):

    colors = {
        'green': '\033[92m',
        'red': '\033[91m',
        'reset': '\033[0m'
    }

    print(f"{colors[color]}{message}{colors['reset']}", end=' ')

