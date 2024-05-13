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
num_li = list(map(int, sys.stdin.readline().rstrip().split()))

sort_li = sorted(list(enumerate(num_li)), key = lambda x : x[1])

min_num = min(num_li)
ii = 0

for _ in range(roof):
    if sort_li[_][1] > min_num:
        ii +=1
        num_li[sort_li[_][0]] = ii
        min_num = sort_li[_][1]
    else:
        num_li[sort_li[_][0]] = ii
print(*num_li)