x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())
if x2 - x1 == y2 - y1:
    print('YES')
elif x2 - x1 == y1 - y2:
    print('YES')
elif (x1 == x2) or (y1 == y2):
    print('YES')
else:
    print('NO')
