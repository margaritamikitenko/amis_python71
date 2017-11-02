class1 = int(input('enter the number of student of the first class'))
class2 = int(input('enter the number of students of the second class'))
class3 = int(input('enter the number of students of the third class'))
z = class1%2 + class2%2 + class3%2 + class1//2 + class2//2 + class3//2
print(z)
