a = int(input())
z = set(range(1,a+1))
while a !='HELP':
    a = input()
    if a=='HELP':
        break
    if a[0] != 'H':
        n = [int(i) for i in a.split()]
    b = input()
    if type(n[0])==int:
        if b =='NO':
            p = z.difference(set(n))
        elif b == 'YES':
            p = z & set(n)
    z = p
print(*z)
