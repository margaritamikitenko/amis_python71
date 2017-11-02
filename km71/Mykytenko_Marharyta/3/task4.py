balls = int(input('Enter number of balls'))
list = []
for i in range(balls):
    list.append(i+1)
list1 = []
throws = int(input('Enter number of throws'))
for j in range(throws):
    list1 += list[int(input('Enter number of the left ball'))-1:int(input('Enter number of the righr ball'))]
for element1 in list1:
    for element2 in list:
        if element2 == element1:
            a = list.index(element2)
            list.insert(a,'.')
            list.remove(element2)
for element2 in list:
    if element2 != '.':
        b = list.index(element2)
        list.insert(b, 'I')
        list.remove(element2)
print(' '.join(list))
