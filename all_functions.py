import time

def count(s):
    dicti = {}
    n = [c for c in s.lower() if c not in ' ., ']
    for c in n:
        if c in dicti:
            dicti[c] += 1
        else:
            dicti[c] = 1
    return dicti

def union(dict1, dict2):
    dici = {}
    for keys, values in dict2.items():
        dici[keys] = values
    for keys, values in dict1.items():
        dici[keys] = values
    return dici

def is_prime(n, primes_minor_than_n):
    for p in primes_minor_than_n:
        if n%p == 0:
            return False
    return True

def generate_primes(until):
    primes = []
    for i in range(2, until):
        if is_prime(i, primes):
            primes.append(i)
    return primes

def descompose(n):
    l = generate_primes(n)
    elements_factor_exponent = {}
    for c in l:
        while n%c == 0:
            if c in elements_factor_exponent:
                elements_factor_exponent[c] += 1
            else:
                elements_factor_exponent[c] = 1
            n = n//c
    return elements_factor_exponent

def print_descom(d, mult =' · '):
    sir = [f"{k}^{v}" for k, v in d.items()]
    return 'mult'.join(sir)

def setInterval(start, ends):
    while start < ends:
        print(start)
        begin += 1
        time.sleep(1)
    print(ends)

def timer(time):
    begin = 1
    while begin < time:
        print(begin)
        begin += 1
        time.sleep(1)
    print(time)

# If you want me to add something just tell me on github