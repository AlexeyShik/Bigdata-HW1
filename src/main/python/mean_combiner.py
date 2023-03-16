#!/usr/bin/python
# -*-coding:utf-8 -*

import sys

sum = 0
count = 0

for line in sys.stdin:
    value = int(line)
    sum += value
    count += 1

result = str(sum) + "," + str(count)
print(result)
