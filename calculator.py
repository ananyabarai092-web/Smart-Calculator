import math
import random


def add(a: float, b: float) -> float:
    return a + b


def subtract(a: float, b: float) -> float:
    return a - b


def multiply(a: float, b: float) -> float:
    return a * b


def divide(a: float, b: float) -> float:
    if b == 0:
        raise ValueError('Division by zero is not allowed.')
    return a / b


def power(a: float, b: float) -> float:
    return math.pow(a, b)


def modulus(a: float, b: float) -> float:
    if b == 0:
        raise ValueError('Modulus by zero is not allowed.')
    return a % b


def square_root(value: float) -> float:
    if value < 0:
        raise ValueError('Negative square root is not allowed.')
    return math.sqrt(value)


def percentage(value: float, percent: float) -> float:
    return (value * percent) / 100.0


def factorial(value: int) -> int:
    if value < 0:
        raise ValueError('Factorial is not defined for negative values.')
    return math.factorial(value)


def average(values: list[float]) -> float:
    if not values:
        raise ValueError('At least one number is required to calculate the average.')
    return sum(values) / len(values)


def calculate_bmi(weight: float, height: float) -> tuple[float, str]:
    if height <= 0:
        raise ValueError('Height must be greater than zero.')
    bmi = weight / (height ** 2)
    category = 'Underweight'
    if bmi >= 18.5 and bmi < 25:
        category = 'Normal Weight'
    elif bmi >= 25 and bmi < 30:
        category = 'Overweight'
    elif bmi >= 30:
        category = 'Obesity'
    return round(bmi, 2), category


def calculate_emi(principal: float, annual_rate: float, duration_months: int) -> tuple[float, float, float]:
    if principal <= 0 or annual_rate < 0 or duration_months <= 0:
        raise ValueError('Loan amount, interest rate, and duration must be positive values.')
    monthly_rate = annual_rate / 1200.0
    if monthly_rate == 0:
        monthly_payment = principal / duration_months
    else:
        monthly_payment = principal * monthly_rate / (1 - (1 + monthly_rate) ** (-duration_months))
    total_payment = monthly_payment * duration_months
    total_interest = total_payment - principal
    return round(monthly_payment, 2), round(total_payment, 2), round(total_interest, 2)


def scientific_sin(value: float) -> float:
    return round(math.sin(math.radians(value)), 6)


def scientific_cos(value: float) -> float:
    return round(math.cos(math.radians(value)), 6)


def scientific_tan(value: float) -> float:
    return round(math.tan(math.radians(value)), 6)


def scientific_log(value: float) -> float:
    if value <= 0:
        raise ValueError('Logarithm is defined only for positive values.')
    return round(math.log10(value), 6)


def scientific_ln(value: float) -> float:
    if value <= 0:
        raise ValueError('Natural logarithm is defined only for positive values.')
    return round(math.log(value), 6)


def scientific_exp(value: float) -> float:
    return round(math.exp(value), 6)


def memory_add(memory: dict, value: float) -> float:
    memory['value'] += value
    return memory['value']


def memory_subtract(memory: dict, value: float) -> float:
    memory['value'] -= value
    return memory['value']


def memory_recall(memory: dict) -> float:
    return memory['value']


def memory_clear(memory: dict) -> float:
    memory['value'] = 0.0
    return memory['value']


def random_number(min_value: int, max_value: int) -> int:
    if min_value > max_value:
        raise ValueError('Minimum value cannot be greater than maximum value.')
    return random.randint(min_value, max_value)
