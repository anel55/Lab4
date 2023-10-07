a = set(input().split())
b = set(input().split())
c = sorted(list(map(int, (a & b))))
print(*c)
