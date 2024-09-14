def is_prime(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        for div in range(2, result):
            if result % div == 0:
                print(f'Составное (первый делитель {result}:{div}={result/div:.0f})')
                return result
        print('Простое')
        return result
    return wrapper

@is_prime
def sum_three(x, y, z):
    return x + y + z

result = sum_three(2, 3, 6)
print(result)
