a = int(input())

b = set()

for i in range(a):
    b.update(input().split())

print(len(b))
