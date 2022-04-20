# Python 3.9.2
N = input();
for x in range(int(N)):
    a, b = input().split()
    print(min(int(a), int(b)), end=' ')