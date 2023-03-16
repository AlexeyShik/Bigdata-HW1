#!/usr/bin/python
# -*-coding:utf-8 -*

import sys

price_pos = 9

for line in sys.stdin:
    words = line.split(",")
    price = words[price_pos]
    print(price)
