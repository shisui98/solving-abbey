# Ben Schroeder, 2014, modified for python 3.9.2 by shisui98
inte = int(input('number of pairs: '))

for i in range(inte):
    a, b = input('pairs: ').split()
    print(int(a) + int(b))