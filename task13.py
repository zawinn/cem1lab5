def fib(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


def fib_adding(n):
    for i in n:
        tmp = i + 10
        yield tmp
generator = fib(10)
new_genertor = fib_adding(generator)
for i in new_genertor:
    print(i)