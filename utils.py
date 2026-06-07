import os
from datetime import datetime

try:
    from colorama import init, Fore, Style
    init(autoreset=True)
except ImportError:
    class Dummy:
        def __getattr__(self, name):
            return ''
    Fore = Style = Dummy()

THEMES = {
    'dark': {
        'primary': Fore.CYAN,
        'secondary': Fore.MAGENTA,
        'success': Fore.GREEN,
        'warning': Fore.YELLOW,
        'error': Fore.RED,
        'info': Fore.WHITE,
    },
    'light': {
        'primary': Fore.BLUE,
        'secondary': Fore.MAGENTA,
        'success': Fore.GREEN,
        'warning': Fore.YELLOW,
        'error': Fore.RED,
        'info': Fore.BLACK,
    },
}

current_theme = 'dark'


def set_theme(theme_name: str):
    global current_theme
    if theme_name in THEMES:
        current_theme = theme_name
    else:
        current_theme = 'dark'


def color_text(text: str, role: str = 'primary') -> str:
    palette = THEMES.get(current_theme, THEMES['dark'])
    return f"{palette.get(role, Fore.WHITE)}{text}{Style.RESET_ALL}"


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_timestamp():
    now = datetime.now()
    return now.strftime('%Y-%m-%d'), now.strftime('%H:%M:%S')


def show_header(title: str, width: int = 40):
    border = '=' * width
    print(color_text(border, 'secondary'))
    title_line = title.center(width)
    print(color_text(title_line, 'primary'))
    print(color_text(border, 'secondary'))


def prompt_text(prompt: str, allow_empty: bool = False) -> str:
    while True:
        value = input(color_text(f'{prompt}: ', 'info')).strip()
        if value or allow_empty:
            return value
        print(color_text('Error: Input cannot be empty. Please try again.', 'error'))


def prompt_number(
    prompt: str,
    value_type=float,
    allow_zero=True,
    allow_negative=True,
    allow_empty=False,
):
    while True:
        value = input(color_text(f'{prompt}: ', 'info')).strip()
        if not value:
            if allow_empty:
                return None
            print(color_text('Error: Input cannot be empty. Please enter a value.', 'error'))
            continue
        try:
            number = value_type(value)
            if not allow_zero and number == 0:
                print(color_text('Error: Zero is not allowed for this value.', 'error'))
                continue
            if not allow_negative and number < 0:
                print(color_text('Error: Negative values are not allowed for this value.', 'error'))
                continue
            return number
        except ValueError:
            print(color_text('Error: Invalid number format. Please enter a valid numeric value.', 'error'))


def prompt_number_list(prompt: str) -> list[float]:
    while True:
        raw = input(color_text(f'{prompt} (comma-separated): ', 'info')).strip()
        if not raw:
            print(color_text('Error: Please enter at least one number.', 'error'))
            continue
        tokens = [item.strip() for item in raw.split(',') if item.strip()]
        if not tokens:
            print(color_text('Error: Please enter valid numeric values separated by commas.', 'error'))
            continue
        try:
            return [float(token) for token in tokens]
        except ValueError:
            print(color_text('Error: Invalid list format. Only numbers are allowed.', 'error'))


def pause(message: str = 'Press Enter to continue...'):
    input(color_text(message, 'secondary'))


def prompt_menu_choice(options: list, prompt_message: str = 'Choose an option') -> int:
    while True:
        choice = input(color_text(f'{prompt_message}: ', 'info')).strip()
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return int(choice)
        print(color_text('Error: Invalid menu choice. Select a valid option number.', 'error'))


def confirm_action(prompt: str) -> bool:
    response = input(color_text(f'{prompt} (y/n): ', 'warning')).strip().lower()
    return response in ('y', 'yes')
