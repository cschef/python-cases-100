# Example 006

## Description

斐波那契数列。

## Analysis

斐波那契数列（Fibonacci sequence），又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。

> 在数学上，费波那契数列是以递归的方法来定义：
F0 = 0      (n=0)
F1 = 1      (n=1)
Fn = F[n-1]+ F[n-2] (n=>2)

## Source

```python
# -*- coding: utf-8 -*-

def fib(n):
    if n == 0 or n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

n = raw_input()
print fib(int(n))
```

```python
# -*- coding: utf-8 -*-

def fib(n):
    if n == 0:
        return [1]
    elif n == 1:
        return [1, 1]
    else:
        list = [1, 1]
        for i in range(2, n + 1):
            list.append(list[-1] + list[-2])
        return list

n = raw_input()
print fib(int(n))
```

```python
# -*- coding: utf-8 -*-

def fib(n):
    a, b = 1, 1
    while n:
        a, b, n = b, a + b, n - 1
        print str(a),

n = raw_input()
fib(int(n))
```
