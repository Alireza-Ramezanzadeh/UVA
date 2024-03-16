t = int(input())

for i in range(t):
    a = list(map(int, input().split(' ')))
    a.sort()
    print(f'Case {i + 1}: {a[1]}')
