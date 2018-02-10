# -*- coding: utf-8 -*-

def fib(n):
    a, b = 1, 1
    while n:
        a, b, n = b, a + b, n - 1
        print str(a),

n = raw_input()
fib(int(n))
