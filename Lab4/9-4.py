a = set()
for i in range(int(input())):
    t = int(input())
    f = {input() for j in range(t)}
    a|=f
print(len(f))
print('\n'.join(str(n)for n in f))
print(len(a))
print(*sorted((c)for c in a))
