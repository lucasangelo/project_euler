#!usr/bin/env/python3

def fibonacci(limit):
    atual = 1
    ant = 0
    fib = 1
    total = 0
    while atual < limit:
        if ant > 0:
            fib = atual + ant
        if fib % 2 == 0:
            total += fib
        ant = atual
        atual = fib
    return total

print (fibonacci(4000000))
