n, k = [int(i) for i in input().split()]
A=set()
for i in range(k):
    a_i, b_i = [int(i) for i in input().split()]
    while a_i < n+1:
        if a_i%7!=0 and a_i%7!=6:
            A.add(a_i)
        a_i+=b_i
print(len(A))
