import math
import re
from Calculator import calculator
from file_manager import file

def generator(pathname, text_mode):
    with file(pathname, text_mode) as action:
        for line in action:  
            yield line

def calculations(operation, args):
    if operation == '+':
        return calculator().add(float(args[0]), float(args[1]))
    elif operation == '-':
        return calculator().subtract(float(args[0]), float(args[1]))
    elif operation == '*':
        return calculator().multiply(float(args[0]), float(args[1]))
    elif operation == '/':
        return calculator().divide(float(args[0]), float(args[1]))
    
count = 0
for i in generator('test.txt', 'r'):
    count += 1
    pattern = r'[-+*/\n]'
    operation = re.findall(pattern, i)
    calculating_list = re.split(pattern, i)
    action = calculations(operation[0], calculating_list)
    print(f"Строчка {count}. Вычисления: {calculating_list[0]} {operation[0]} {calculating_list[1]} = {action}")
    




