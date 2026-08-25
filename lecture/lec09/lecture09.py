def split(n):
    return n // 10, n % 10

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

def cascade_v1(n):
    if n < 10:
        print(n)
    else:
        print(n)
        cascade_v1(n//10)
        print(n)

def cascade_v2(n):
    print(n)
    if n >= 10:
        cascade_v2(n//10)
        print(n)

def inverse_cascade(n):
    if n < 10:
        print(n)
    else:
        grow(n//10)
        print(n)
        shirnk(n//10)  
        
def grow(n):
    if n >= 10:
        grow(n//10)
    print(n)

def shirnk(n):
    if n < 10:
        print(n)
    else:
        print(n)
        shirnk(n//10)

def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 2) + fib(n - 1)

def counting_partitions(n, m):
    if n == 0: 
        return 1
    if n < 0 or m == 0:
        return 0
    return counting_partitions(n - m, m) + counting_partitions(n, m-1)