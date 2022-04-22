#!/usr/bin/env python
# Fahrenheit to Celsius
from decimal import Decimal, ROUND_HALF_UP
inte = input().split();
a_list = [int(x) for x in inte];
for i in a_list[1:]:
    num = ((i - 32) * (5/9))
    num = Decimal(num).quantize(0, ROUND_HALF_UP)
    print(num, end=' ')

# x = int(cel//1 + ((cel%1)/0.5)//1)
# must investigate!
