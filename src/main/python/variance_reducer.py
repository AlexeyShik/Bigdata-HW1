#!/usr/bin/python
# -*-coding:utf-8 -*

import sys

sum = 0
sum2 = 0
count = 0

for line in sys.stdin:
    values = line.split(",")
    cur_sum = int(values[0])
    cur_sum2 = int(values[1])
    cur_count = int(values[2])
    sum += cur_sum
    sum2 += cur_sum2
    count += cur_count

mean = sum / count
mean2 = sum2 / count
variance = mean2 - mean ** 2
print(variance)
