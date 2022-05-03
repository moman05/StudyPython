# * 찍기
for x in range(1, 6):
    for y in range(x, 6, 1):
        print(' ', end='')

    for y in range(1, x):
        print('*', end='')

    print('')

print('Hello', end=', ')
print('world')