from itertools import islice, count


def fibo():
    a, b = 1, 1
    while True:
        a, b = b, a+b
        yield a


def gen_n_fibo(n):
    return next(islice(fibo(), n-1, n))


print(gen_n_fibo(5))
