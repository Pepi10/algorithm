# import sys
# s_roof, test_roof = list(map(int, sys.stdin.readline().rstrip().split(' ')))

# s_set = list()
# test_set = list()
# for _ in range(s_roof):
#     s_set.append(sys.stdin.readline().rstrip())
# for _ in range(test_roof):
#     test_set.append(sys.stdin.readline().rstrip())

# def selection(list, target):
#     list.sort()
#     l, r = 0, len(list) - 1
#     while l <= r:
#         center = (l + r) // 2
#         if list[center] == target:
#             return True
#         elif list[center] < target:
#             l = center + 1
#         else:
#             r = center - 1
#     return False

# i = 0
# for val in test_set:
#     if selection(s_set, val) == True:
#         i += selection(s_set, val)
    
# print(i)

import sys

s_roof, test_roof = list(map(int, sys.stdin.readline().rstrip().split(' ')))

s_set = [0] * s_roof
test_set = [0] * test_roof
for _ in range(s_roof):
    s_set[_] = sys.stdin.readline().rstrip()
for _ in range(test_roof):
    test_set[_] = sys.stdin.readline().rstrip()

def selection(list, target):
    list.sort()
    l, r = 0, len(list) - 1
    while l <= r:
        center = (l + r) // 2
        if list[center] == target:
            return True
        elif list[center] < target:
            l = center + 1
        else:
            r = center - 1
    return False

res = [0] * test_roof
for ind, val in enumerate(test_set):
    if selection(s_set, val):
        res[ind] = 1

print(sum(res))