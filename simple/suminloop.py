# Sum in loop, general solution, python 3.9.2
a, b = (input('start and end points for slicing: ').split());
list1 = [int(x) for x in input('list input: ').split()];
list2 = list1[int(a):int(b)];
print(sum(list2));

