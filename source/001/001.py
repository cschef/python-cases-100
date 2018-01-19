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
