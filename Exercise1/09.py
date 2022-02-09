a, h = int(input()), int(input())
print(' ' * (h - 1) + '*' * a)
for i in range(h - 2, 0, -1):
    print(' ' * i + '*' + ' ' * (a - 2) + '*')
print('*' * a)