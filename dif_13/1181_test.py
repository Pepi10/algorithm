import sys

roof = int(sys.stdin.readline().rstrip())

temp_di = {}
for _ in range(roof):
    val = sys.stdin.readline().rstrip()
    ind = len(val)
    if ind not in temp_di:
        temp_di[ind] = []
    if val in temp_di[ind]:
        pass 
    else:
        temp_di[ind].append(val)

for ind in sorted(temp_di):
    for val in sorted(temp_di[ind]):
        print(val)