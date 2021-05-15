def fibonacci(n):
    """ The function takes as input the number n, returns the n'th number of
    the Fibonacci sequence"""
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)


if __name__ == '__main__':
    print(fibonacci(0))
    print(fibonacci(7))
