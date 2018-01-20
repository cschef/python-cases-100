# Example 005

## Description

输入三个整数x,y,z，请把这三个数由小到大输出。

## Analysis

我们想办法把最小的数放到x上，先将x与y进行比较，如果x>y则将x与y的值进行交换，然后再用x与z进行比较，如果x>z则将x与z的值进行交换，这样能使x最小。

## Source

```python
# -*- coding: utf-8 -*-

a = int(raw_input())
b = int(raw_input())
c = int(raw_input())

if a > b:
    a, b = b, a
if b > c:
    b, c = c, b
if a > b:
    a, b = b, a

print a, b, c
```

```python
# -*- coding: utf-8 -*-

l = []

for i in range(3):
    x = int(raw_input())
    l.append(x)

l.sort()
print l
```

```python
# -*- coding: utf-8 -*-

print( sorted( [int(raw_input()) for x in range(3)]))
```
