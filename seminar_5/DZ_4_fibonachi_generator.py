# Создайте функцию генератор чисел Фибоначчи

def fibonachi_generator(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


num_terms = 10

print(list(fibonachi_generator(num_terms)))
