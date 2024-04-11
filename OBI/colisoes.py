coord1 = [int(i) for i in input().split()]
coord2 = [int(i) for i in input().split()]


if coord1[2] < coord2[0] or coord1[0] > coord2[2] or coord1[3] < coord2[1] or coord1[1] > coord2[3]:
    print('0')
else:
    print('1')