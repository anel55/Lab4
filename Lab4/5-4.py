n, m = [int(i) for i in input().split()]
a_set, b_set = set(), set()
for i in range(n):
    a_set.add(int(input()))
for i in range(m):
    b_set.add(int(input()))
    
def p(a):
    print(len(a))
    print(' '.join(([str(i) for i in sorted(a)])))
    
p(a_set & b_set)
p(a_set - b_set)
p(b_set - a_set)
