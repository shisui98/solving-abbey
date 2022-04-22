# Rounding, python 3.9.2
from decimal import Decimal, ROUND_HALF_UP
N = input();
for i in range(int(N)):
    a, b = input().split();
    X = (int(a)/int(b));
    X = (float("%.02f" % X));
    X = Decimal(X).quantize(0, ROUND_HALF_UP)
    print(X, end=" ");
