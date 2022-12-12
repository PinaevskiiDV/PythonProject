
num = int(input())

def fib(n):
    if n == 0 or n == 1:
        return n
    return fib(n - 1) + fib(n - 2)

def lst_nfib_fib(n):
    lst_fib = []
    for e in range(1, n + 1):
        lst_fib.append(fib(e))
    lst_fib.insert(0, 0)
    for e in range(1, n + 1):
        lst_fib.insert(0, (-1) ** (e + 1) * fib(e))
    return lst_fib


print(lst_nfib_fib(num))