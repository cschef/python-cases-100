# Example 004

## Description

输入某年某月某日，判断这一天是这一年的第几天？

## Analysis

以3月5日为例，应该先把前两个月的加起来，然后再加上5天即本年的第几天，特殊情况，闰年且输入月份大于2时需考虑多加一天：

## Source

```python
# -*- coding: utf-8 -*-

# 输入年月日
y = int(raw_input())
m = int(raw_input())
d = int(raw_input())

# 月份天数
months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31, 0]

days = 0

# 闰年情况
if (y % 400 == 0) or (y % 4 == 0 and y % 100 != 0):
    months[2] = 29

days += sum(months[1 : m])

days += d

print days
```

```python
# -*- coding: utf-8 -*-

import time

D = raw_input("Input date (eg.2018-01-20): ")
d = time.strptime(D, '%Y-%m-%d').tm_yday
print '{}'.format(d)
```

```python
# -*- coding: utf-8 -*-

import time

D=raw_input("Input date (eg.2018-01-20): ")
print(time.strptime(D, '%Y-%m-%d')[7])
```

```python
# -*- coding: utf-8 -*-

import time
import sys

reload(sys)
sys.setdefaultencoding('utf-8')  # 设置 'utf-8'
a = raw_input("Input date (eg.2018-01-20): ")
t = time.strptime(a,"%Y-%m-%d")
print int(time.strftime("%j",t).decode('utf-8'))
```
