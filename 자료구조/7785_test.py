import sys

def search(list, target):
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

roof = int(sys.stdin.readline().rstrip())

enter = {0: [], 1: []}
for _ in range(roof):
    name, stat = list(sys.stdin.readline().rstrip().split(' '))
    if stat == "enter":
        enter[1] += [name]
    else:
        enter[0] += [name]

for val in enter[1]:
    if search(enter[0], val) == False:
        print(val)