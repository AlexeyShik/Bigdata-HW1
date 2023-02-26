#!/usr/bin/python
# -*-coding:utf-8 -*

import sys

sum = 0
sum2 = 0
count = 0

for line in sys.stdin:
    value = int(line)
    sum += value
    sum2 += value ** 2
    count += 1

result = str(sum) + "," + str(sum2) + "," + str(count)
print(result)
