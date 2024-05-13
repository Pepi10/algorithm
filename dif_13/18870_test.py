# import sys

# _ = sys.stdin.readline().rstrip()
# num_li = list(map(int, sys.stdin.readline().rstrip().split(' ')))
# sorted_li = sorted(num_li)

# print(sorted_li)

# temp_dict = dict()
# ii = 0
# for val in sorted_li:
#     if val in list(temp_dict.keys()):
#         pass
#     else:
#         temp_dict[val] = ii
#         ii += 1

# print(temp_dict)
# print(num_li)

# res = list()
# for num in num_li:
#     res.append(temp_dict[num])

# print(*res)

import sys

_ = sys.stdin.readline().rstrip()
num_li = list(map(int, sys.stdin.readline().rstrip().split(' ')))
sort_li = sorted(set(num_li))
temp_di = dict()

for ind, val in enumerate(sort_li):
    temp_di[val] = ind

res = list()

for num in num_li:
    res.append(temp_di[num])
print(*res)