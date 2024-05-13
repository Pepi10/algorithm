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

roof = int(sys.stdin.readline().rstrip())

temp_di = {}
for _ in range(roof):
    val = sys.stdin.readline().rstrip()
    ind = len(val)
    if ind not in temp_di:
        temp_di[ind] = []
    temp_di[ind].append(val)

for ind in sorted(temp_di):
    for val in sorted(temp_di[ind]):
        print(val)