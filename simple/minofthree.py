# Minimum of three, python 3.9.2
N = input();
for x in range(int(N)):
    a, b, c = input().split()
    print(min(int(a), int(b), int(c)), end=" ")

# choosing minimum efficiently:
# trick 1:
# min=a;
# if(min>b)
#     min=b;
# if(min>c)
#     min=c;
# // output min

# trick 2:
# if (a < b)
#     b = a;
# if (b < c)
#     c = b;
# // output c
