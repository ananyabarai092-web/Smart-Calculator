import os
import sys

import calculator
import history
import profiles
import statistics as stats
import utils
from utils import (
    clear_console,
    color_text,
    confirm_action,
    pause,
    prompt_menu_choice,
    prompt_number,
    prompt_number_list,
    prompt_text,
    set_theme,
    show_header,
)

memory_state = {'value': 0.0}
current_user = None

MENU_OPTIONS = [
    'Addition',
    'Subtraction',
    'Multiplication',
    'Division',
    'Power',
    'Modulus',
    'Square Root',
    'Percentage Calculator',
    'Factorial',
    'Average Calculator',
    'BMI Calculator',
    'EMI Calculator',
    'Scientific Calculator',
    'Random Number Generator',
    'View History',
    'Clear History',
    'Statistics Dashboard',
    'User Profile',
    'Exit',
]


def initialize_files():
    directory = os.path.dirname(__file__)
    for filename, default_content in [
        ('history.json', '[]'),
        ('users.json', '{}'),
    ]:
        path = os.path.join(directory, filename)
        if not os.path.exists(path):
            with open(path, 'w', encoding='utf-8') as handle:
                handle.write(default_content)


def display_main_menu():
    clear_console()
    show_header('SMART CALCULATOR')
    print(color_text('Welcome to the professional terminal calculator experience.', 'info'))
    print(color_text('Theme:', 'secondary'), color_text(utils.current_theme.title(), 'primary'))
    print()
    for index, option in enumerate(MENU_OPTIONS, start=1):
        print(color_text(f'{index:2}.', 'secondary'), color_text(option, 'info'))
    print()


def display_result(operation: str, result, inputs: list):
    show_header('CALCULATION RESULT')
    print(color_text(f'Operation : {operation}', 'secondary'))
    print(color_text(f'Inputs    : {inputs}', 'secondary'))
    print(color_text(f'Result    : {result}', 'success'))
    print(color_text('=', 'secondary') * 34)
    pause()


def record_history(operation: str, inputs: list, result):
    user_id = current_user['username'] if current_user else None
    history.add_record(operation, inputs, result, user_id)
    if current_user:
        profiles.update_after_calculation(current_user, operation)


def get_user_choice():
    return prompt_menu_choice(MENU_OPTIONS)


def perform_two_operand(operation_name: str, operation_func, first_prompt: str, second_prompt: str, allow_zero_second: bool = True):
    first_value = prompt_number(first_prompt)
    second_value = prompt_number(second_prompt, allow_zero=allow_zero_second)
    try:
        result = operation_func(first_value, second_value)
        display_result(operation_name, result, [first_value, second_value])
        record_history(operation_name, [first_value, second_value], result)
    except Exception as error:
        print(color_text(f'Error: {error}', 'error'))
        pause()


def perform_single_operand(operation_name: str, operation_func, prompt_label: str, allow_negative: bool = True):
    value = prompt_number(prompt_label, allow_negative=allow_negative)
    try:
        result = operation_func(value)
        display_result(operation_name, result, [value])
        record_history(operation_name, [value], result)
    except Exception as error:
        print(color_text(f'Error: {error}', 'error'))
        pause()


def addition():
    values = prompt_number_list('Enter numbers to add')
    result = sum(values)
    display_result('Addition', result, values)
    record_history('Addition', values, result)


def subtraction():
    perform_two_operand('Subtraction', calculator.subtract, 'Enter first number', 'Enter second number')


def multiplication():
    values = prompt_number_list('Enter numbers to multiply')
    result = 1
    for value in values:
        result *= value
    display_result('Multiplication', result, values)
    record_history('Multiplication', values, result)


def division():
    perform_two_operand('Division', calculator.divide, 'Enter dividend', 'Enter divisor', allow_zero_second=False)


def power():
    perform_two_operand('Power', calculator.power, 'Enter base', 'Enter exponent')


def modulus():
    perform_two_operand('Modulus', calculator.modulus, 'Enter first number', 'Enter second number', allow_zero_second=False)


def square_root():
    perform_single_operand('Square Root', calculator.square_root, 'Enter number', allow_negative=False)


def percentage_calculator():
    value = prompt_number('Enter base value')
    percent = prompt_number('Enter percentage value')
    result = calculator.percentage(value, percent)
    display_result('Percentage', result, [value, percent])
    record_history('Percentage', [value, percent], result)


def factorial_calculator():
    value = prompt_number('Enter integer value', value_type=int, allow_negative=False)
    try:
        result = calculator.factorial(value)
        display_result('Factorial', result, [value])
        record_history('Factorial', [value], result)
    except Exception as error:
        print(color_text(f'Error: {error}', 'error'))
        pause()


def average_calculator():
    values = prompt_number_list('Enter numbers to average')
    try:
        result = calculator.average(values)
        display_result('Average Calculator', result, values)
        record_history('Average Calculator', values, result)
    except Exception as error:
        print(color_text(f'Error: {error}', 'error'))
        pause()


def bmi_calculator():
    weight = prompt_number('Enter weight in kilograms', allow_negative=False, allow_zero=False)
    height = prompt_number('Enter height in meters', allow_negative=False, allow_zero=False)
    try:
        result, category = calculator.calculate_bmi(weight, height)
        display_result('BMI Calculator', f'{result} ({category})', [weight, height])
        record_history('BMI Calculator', [weight, height], result)
    except Exception as error:
        print(color_text(f'Error: {error}', 'error'))
        pause()


def emi_calculator():
    principal = prompt_number('Enter loan amount', allow_negative=False, allow_zero=False)
    annual_rate = prompt_number('Enter annual interest rate (%)', allow_negative=False)
    duration = prompt_number('Enter duration in months', value_type=int, allow_negative=False, allow_zero=False)
    try:
        monthly_payment, total_payment, total_interest = calculator.calculate_emi(principal, annual_rate, duration)
        display_result('EMI Calculator', f'Monthly: {monthly_payment}, Total: {total_payment}, Interest: {total_interest}', [principal, annual_rate, duration])
        record_history('EMI Calculator', [principal, annual_rate, duration], monthly_payment)
    except Exception as error:
        print(color_text(f'Error: {error}', 'error'))
        pause()


def scientific_calculator():
    options = [
        'sin()',
        'cos()',
        'tan()',
        'log()',
        'ln()',
        'exp()',
        'sqrt()',
        'Memory Operations',
        'Back to Main Menu',
    ]
    while True:
        clear_console()
        show_header('SCIENTIFIC CALCULATOR')
        for index, option in enumerate(options, start=1):
            print(color_text(f'{index:2}.', 'secondary'), color_text(option, 'info'))
        choice = prompt_menu_choice(options, 'Choose a scientific feature')
        if choice == 1:
            perform_single_operand('sin()', calculator.scientific_sin, 'Enter degrees')
        elif choice == 2:
            perform_single_operand('cos()', calculator.scientific_cos, 'Enter degrees')
        elif choice == 3:
            perform_single_operand('tan()', calculator.scientific_tan, 'Enter degrees')
        elif choice == 4:
            perform_single_operand('log()', calculator.scientific_log, 'Enter positive value', allow_negative=False)
        elif choice == 5:
            perform_single_operand('ln()', calculator.scientific_ln, 'Enter positive value', allow_negative=False)
        elif choice == 6:
            perform_single_operand('exp()', calculator.scientific_exp, 'Enter value')
        elif choice == 7:
            perform_single_operand('sqrt()', calculator.scientific_sqrt, 'Enter non-negative value', allow_negative=False)
        elif choice == 8:
            memory_operations_menu()
        else:
            break


def memory_operations_menu():
    options = ['M+ (Add)', 'M- (Subtract)', 'MR (Recall)', 'MC (Clear)', 'Back']
    while True:
        clear_console()
        show_header('MEMORY FUNCTIONS')
        print(color_text(f'Memory Value: {memory_state["value"]}', 'success'))
        for index, option in enumerate(options, start=1):
            print(color_text(f'{index:2}.', 'secondary'), color_text(option, 'info'))
        choice = prompt_menu_choice(options, 'Choose memory operation')
        if choice == 1:
            value = prompt_number('Enter value for M+ to add')
            new_value = calculator.memory_add(memory_state, value)
            record_user_memory_usage()
            print(color_text(f'Memory updated: {new_value}', 'success'))
            pause()
        elif choice == 2:
            value = prompt_number('Enter value for M- to subtract')
            new_value = calculator.memory_subtract(memory_state, value)
            record_user_memory_usage()
            print(color_text(f'Memory updated: {new_value}', 'success'))
            pause()
        elif choice == 3:
            print(color_text(f'Memory Recall: {calculator.memory_recall(memory_state)}', 'success'))
            pause()
        elif choice == 4:
            calculator.memory_clear(memory_state)
            record_user_memory_usage()
            print(color_text('Memory cleared successfully.', 'success'))
            pause()
        else:
            break


def record_user_memory_usage():
    if current_user:
        profiles.update_memory_usage(current_user)


def random_number_generator():
    min_value = prompt_number('Enter minimum value', value_type=int)
    max_value = prompt_number('Enter maximum value', value_type=int)
    if min_value > max_value:
        print(color_text('Error: Minimum value cannot be greater than maximum value.', 'error'))
        pause()
        return
    try:
        result = calculator.random_number(min_value, max_value)
        display_result('Random Number Generator', result, [min_value, max_value])
        record_history('Random Number Generator', [min_value, max_value], result)
    except Exception as error:
        print(color_text(f'Error: {error}', 'error'))
        pause()


def view_history_menu():
    while True:
        records = history.load_history()
        clear_console()
        show_header('CALCULATION HISTORY')
        if not records:
            print(color_text('No history records found.', 'warning'))
        else:
            for index, record in enumerate(records, start=1):
                print(color_text(f'{index:2}.', 'secondary'), color_text(f"{record['date']} {record['time']} | {record['operation']} | {record['inputs']} = {record['result']} | User: {record['user']}", 'info'))
        print()
        options = ['Search History', 'Delete Specific Record', 'Back']
        choice = prompt_menu_choice(options)
        if choice == 1:
            keyword = prompt_text('Enter keyword to search in history')
            results = history.search_history(keyword)
            clear_console()
            show_header('SEARCH RESULTS')
            if not results:
                print(color_text('No matches found.', 'warning'))
            else:
                for index, record in enumerate(results, start=1):
                    print(color_text(f'{index:2}.', 'secondary'), color_text(f"{record['date']} {record['time']} | {record['operation']} | {record['inputs']} = {record['result']} | User: {record['user']}", 'info'))
            pause()
        elif choice == 2:
            if not records:
                print(color_text('History is empty. Nothing to delete.', 'warning'))
                pause()
                continue
            index_to_delete = prompt_number('Enter record number to delete', value_type=int, allow_negative=False, allow_zero=False)
            if 1 <= index_to_delete <= len(records):
                if confirm_action('Confirm deletion of selected history record'):
                    success = history.delete_record(index_to_delete - 1)
                    print(color_text('Record deleted successfully.' if success else 'Failed to delete record.', 'success' if success else 'error'))
                else:
                    print(color_text('Deletion cancelled.', 'warning'))
            else:
                print(color_text('Invalid record number. Please try again.', 'error'))
            pause()
        elif choice == 3:
            break


def clear_history_action():
    if confirm_action('Are you sure you want to clear all history?'):
        history.clear_history()
        print(color_text('All history records have been cleared.', 'success'))
    else:
        print(color_text('Clear history cancelled.', 'warning'))
    pause()


def statistics_dashboard():
    records = history.load_history()
    summary = stats.generate_statistics(records)
    clear_console()
    show_header('STATISTICS DASHBOARD')
    print(color_text(f"Total Calculations     : {summary['total_calculations']}", 'info'))
    print(color_text(f"Most Used Operation   : {summary['most_used_operation']}", 'info'))
    print(color_text(f"Highest Result        : {summary['highest_result']}", 'info'))
    print(color_text(f"Lowest Result         : {summary['lowest_result']}", 'info'))
    print(color_text(f"Average Result        : {summary['average_result']}", 'info'))
    print(color_text(f"Last Calculation Time : {summary['last_calculation_time']}", 'info'))
    pause()


def profile_dashboard():
    clear_console()
    show_header('USER PROFILE')
    if not current_user:
        print(color_text('Guest mode is active. Login or register to save activity and earn badges.', 'warning'))
        pause()
        return
    summary = profiles.build_profile_summary(current_user)
    print(color_text(f"Username                 : {summary['username']}", 'info'))
    print(color_text(f"Calculations Performed   : {summary['calculations_performed']}", 'info'))
    print(color_text(f"Favorite Operation       : {summary['favorite_operation']}", 'info'))
    print(color_text(f"Total Sessions           : {summary['total_sessions']}", 'info'))
    print(color_text(f"Memory Functions Used    : {summary['memory_usage']}", 'info'))
    print(color_text('Earned Badges:', 'secondary'))
    for badge in summary['badges']:
        print(color_text(f' - {badge}', 'success'))
    print()
    print(color_text('Press T to toggle theme or Enter to return to the main menu.', 'info'))
    response = input().strip().lower()
    if response == 't':
        toggle_theme()


def toggle_theme():
    new_theme = 'light' if utils.current_theme == 'dark' else 'dark'
    set_theme(new_theme)
    print(color_text(f'Theme changed to {new_theme.title()}.', 'success'))
    pause()


def user_authentication():
    global current_user
    initialize_files()
    while True:
        clear_console()
        show_header('WELCOME')
        print(color_text('1. Login', 'info'))
        print(color_text('2. Register', 'info'))
        print(color_text('3. Continue as Guest', 'info'))
        choice = prompt_menu_choice(['Login', 'Register', 'Guest'], 'Choose a welcome option')
        if choice == 1:
            username = prompt_text('Enter your username')
            try:
                current_user = profiles.login_user(username)
                profiles.update_session(current_user)
                print(color_text(f'Welcome back, {current_user["username"]}!', 'success'))
                pause()
                break
            except ValueError as error:
                print(color_text(f'Error: {error}', 'error'))
                pause()
        elif choice == 2:
            username = prompt_text('Choose a username')
            try:
                current_user = profiles.register_user(username)
                profiles.update_session(current_user)
                print(color_text(f'Thanks for registering, {current_user["username"]}!', 'success'))
                pause()
                break
            except ValueError as error:
                print(color_text(f'Error: {error}', 'error'))
                pause()
        else:
            current_user = None
            print(color_text('Continuing as guest. History is still recorded.', 'warning'))
            pause()
            break


def main():
    set_theme('dark')
    user_authentication()
    while True:
        display_main_menu()
        choice = get_user_choice()
        if choice == 1:
            addition()
        elif choice == 2:
            subtraction()
        elif choice == 3:
            multiplication()
        elif choice == 4:
            division()
        elif choice == 5:
            power()
        elif choice == 6:
            modulus()
        elif choice == 7:
            square_root()
        elif choice == 8:
            percentage_calculator()
        elif choice == 9:
            factorial_calculator()
        elif choice == 10:
            average_calculator()
        elif choice == 11:
            bmi_calculator()
        elif choice == 12:
            emi_calculator()
        elif choice == 13:
            scientific_calculator()
        elif choice == 14:
            random_number_generator()
        elif choice == 15:
            view_history_menu()
        elif choice == 16:
            clear_history_action()
        elif choice == 17:
            statistics_dashboard()
        elif choice == 18:
            profile_dashboard()
        else:
            print(color_text('Thank you for using Smart Calculator. Goodbye!', 'success'))
            sys.exit(0)


if __name__ == '__main__':
    main()
