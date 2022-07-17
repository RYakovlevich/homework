def gen(start, znach):
    while True:
        start = start * znach
        yield start


a = gen(1, 5)
print(next(a))
print(next(a))
print(next(a))


