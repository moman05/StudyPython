# 구구단 프로그램
# 2X1=2 ... 2X9=18   x * y = xy
# 3X1=3 ... 3X9=27
#           9X9=81

print('---구구단 프로그램---')

for x in range(2, 10):
    print(f'{x}단 시작')
    for y in range(1, 10):
        print(f'{x}x{y}={x*y:2d}', end=' ')
    print()  #단마다 줄맞추기 위해서 
