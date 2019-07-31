# Q1 Constantine Theocharis, Python 3.7

angles = [int(i) for i in input().split()]

if sum(angles) != 180:
    print('IMPOSSIBLE')

elif angles[0] == angles[1] == angles[2]:
    print('EQUILATERAL')

elif (angles[0] == angles[1]) or (angles[1] == angles[2]) or (angles[0] == angles[2]):
    print('ISOSCELES')

else:
    print('SCALENE')
