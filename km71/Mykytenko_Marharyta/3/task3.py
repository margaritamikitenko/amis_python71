list = input('Enter your list').split()
for i in range(len(list)):
    list[i] = int(list[i])
list1 = []
for listelem in range(len(list)):
    if list.count(listelem) == 1:
        list1.append(listelem)
print(list1)
