import sys

_ = sys.stdin.readline().rstrip()
my_card = list(map(int, sys.stdin.readline().rstrip().split(' ')))
drop = int(sys.stdin.readline().rstrip())
drop_card = list(map(int, sys.stdin.readline().rstrip().split(' ')))

def binary_search(list, target):
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

my_card.sort()

res = [0] * drop
for ind, val in enumerate(drop_card):
    if binary_search(my_card, val):
        res[ind] = 1
        
print(*res)