from util.special_chars import special_chars

def print_status(status, message = ''):
    green_color = '\033[92m'  # ANSI escape code for green
    red_color = '\033[91m'    # ANSI escape code for red
    reset_color = '\033[0m'   # ANSI escape code to reset color

    if status:
        print(f"{green_color}{special_chars.check}{reset_color}", end=' ')
    else:
        print(f"{red_color}{special_chars.cross}{reset_color}", end=' ')

    if message:
        print(message)