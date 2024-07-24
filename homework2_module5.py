import re
from typing import Callable, Generator

def generator_numbers(text: str) -> Generator[float, None, None]:
    numbers = re.findall(r'(?<=\s)(\d+\.\d+|\d+)(?=\s)', text)
    for number in numbers:
        yield float(number)

def sum_profit(text: str, func: Callable) -> float:
    total = sum(func(text))
    return total

text = "Общий доход работника состоит из нескольких частей: 1500.01 как основной доход, дополненный дополнительными поступлениями 30.01 и 350.01 долларов."
total_income = sum_profit(text, generator_numbers)
print(f"Total income: {total_income:.2f}")
