import random

def random_number_generator(count, min_value, max_value):
    while(count != 0):
        yield random.randint(min_value, max_value)  
        count -= 1

random_iterator = random_number_generator(10, 1, 100)

for num in random_iterator:
    print(num)  
