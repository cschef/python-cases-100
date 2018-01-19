# Example 001

## Description

有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？

## Analysis

可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。

## Source

```python
# -*- coding: utf-8 -*-

count = 0   # 计数

for i in range(1, 5):
    for j in range(1, 5):
        for k in range(1, 5):
            if i != j and j != k and k != i:    # 可以写成 i != j != k != i
                count += 1
                print i * 100 + j * 10 + k

print 'count =', count
```

```python
# -*- coding: utf-8 -*-

count = 0   # 计数

for i in range(1, 5):
    for j in range(1, 5):
        if i == j:      # 减少冗余判断和循环
            continue
        for k in range(1, 5):
            if j != k and k != i:
                count += 1
                print i * 100 + j * 10 + k

print 'count =', count
```

```python
# -*- coding: utf-8 -*-

num = (1, 2, 3, 4)

list = [i * 100 + j * 10 + k \
        for i in num  for j in num for k in num \
        if (j != i and k != j and k != i)]

print list
print 'count =', len(list)
```

```python
# -*- coding: utf-8 -*-

from itertools import permutations

count = 0   # 计数

for i in permutations([1, 2, 3, 4], 3):
    count += 1
    print i[0] * 100 + i[1] * 10 + i[-1]

print 'count =', count
```
