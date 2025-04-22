import random

class RandomNumberIterator:
    def __init__(self, count, min_value, max_value):
        self.count = count       
        self.min_value = min_value  
        self.max_value = max_value
        self.current_count = 0    

    def __iter__(self):
        return self 

    def __next__(self):
        if self.current_count < self.count:
            random_number = random.randint(self.min_value, self.max_value)  
            self.current_count += 1  
            return random_number  
        else:
            raise StopIteration  

random_iterator = RandomNumberIterator(10, 1, 100)

for num in random_iterator:
    print(num)  
