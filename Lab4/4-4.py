a=[int(i) for i in input().split()]
b = set()
for i in range(len(a)):
    if a[i] not in b:
        print('NO')
        b.add(a[i])
    else:
        print('YES')
