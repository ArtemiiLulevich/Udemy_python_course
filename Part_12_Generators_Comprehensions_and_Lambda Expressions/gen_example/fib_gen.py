def fibonacci():
    cur, prev = 0, 1

    while True:
        yield cur
        cur, prev = cur + prev, cur


fib = fibonacci()

for _ in range(20):
    print(next(fib))
