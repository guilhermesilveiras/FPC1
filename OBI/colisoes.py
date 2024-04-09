coord1 = [int(i) for i in input('').split()]
coord2 = [int(i) for i in input('').split()]



if coord1[0] < coord2[0] and coord1[2] < coord2[2] and coord1[0] < coord2[2] and coord1[2] < coord2[0] or coord1[0] > coord2[0] and coord1[2] > coord2[2] and coord1[0] > coord2[2] and coord1[2] > coord2[0]:
    print('0')
else:
    print('1')