for y in range(15,-11,-1):
    y /= 10
    for x in range(-150,150,5):
     x /= 100
     a = x * x + y * y - 1
     if a * a * a - x * x * y * y * y <= 0.0:
        print('*', end = '')
     else:
        print(' ', end = '')
    print()
