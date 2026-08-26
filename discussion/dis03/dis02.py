def skip_factorial(n):
    if n <= 1:
        return 1
    return n * skip_factorial(n - 2)

def swipe(n):
    if n < 10:
        print(n)
    else:
        print(n%10)
        swipe(n//10)
        print(n % 10)

def is_prime(n):
    def check_divisor(k):
        if k * k > n:
            return True
        elif n % k == 0:
            return False
        else:
            return check_divisor(k + 1)

    return n > 1 and check_divisor(2)

def hailstone(n):
    print(n)
    if n == 1:
        return 1
    if n % 2 == 0:
        return even(n)
    else:
        return odd(n)

def even(n):
    return 1 + hailstone(n // 2)

def odd(n):
    return 1 + hailstone(3 * n + 1)


def sevens(n , k):
    def f(i, who, direction): 
        if i == n:
            return who
        if i % 7 == 0 or has_seven(i):
            direction = -direction
        next = who + direction
        if next > k: next = 1
        if next < 1: next = k
        return f(i + 1, next, direction)
    return f(1, 1, 1);

def has_seven(n):
    if n == 0:
        return False
    elif n % 10 == 7:
        return True
    else:
        return has_seven(n // 10)



