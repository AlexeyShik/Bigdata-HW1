#!/usr/bin/python
# -*-coding:utf-8 -*

import sys

sum = 0
count = 0

for line in sys.stdin:
    values = line.split(",")
    cur_sum = values[0]
    cur_count = values[1]
    sum += int(cur_sum)
    count += int(cur_count)

mean = sum / count
print(mean)
