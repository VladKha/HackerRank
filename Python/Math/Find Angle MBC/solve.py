import math

if __name__ == '__main__':
    AB = int(input())
    BC = int(input())
    print('{:.0f}°'.format(math.degrees(math.atan(AB/BC))))
