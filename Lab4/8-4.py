max_n = int(input())
inp = input()
result = set(range(1, max_n+1))
while inp != 'HELP':
    s = set(map(int, inp.split()))
    if len(s & result) <= len(result) / 2:
        answer = 'NO'
    else:
        answer = 'YES'
    print(answer)
    if answer == 'YES':
        result &= s
    elif answer == 'NO':
        result -= s
    inp = input()
print(*sorted(result))
