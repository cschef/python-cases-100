# -*- coding: utf-8 -*-

import time

D=raw_input("Input date (eg.2018-01-20): ")
print(time.strptime(D, '%Y-%m-%d')[7])
