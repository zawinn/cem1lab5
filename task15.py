from time import perf_counter

class Timer:
    def __enter__(self):
        self.start_time = perf_counter()
        return self

    def __exit__(self, type, value, traceback):
        self.end_time = perf_counter()
        self.interval = self.end_time - self.start_time
        print(f"Время выполнения: {self.interval:.6f} секунд")

def fibonacci_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


n = 100000  
with Timer():
    fib_numbers = list(fibonacci_generator(n))
