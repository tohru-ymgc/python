#!/usr/bin/env python
# -*- coding: utf-8 -*-

def fizzbuzz(i):

    if i % 3 == 0 and i % 5 == 0:
        return "fizzbuzz"
    elif i % 3 == 0:
        return "fizz"
    elif i % 5 == 0:
        return "buzz"
    else:
        return i

for i in range(1,101):

    print(fizzbuzz(i))
