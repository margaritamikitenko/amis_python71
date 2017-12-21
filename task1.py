x1 = float(input())
x2 = float(input())
y1 = float(input())
y2 = float(input())#Вводимо по черзі координати двох точок
def distance(x1, x2, y1, y2):
    return(((x2-x1)**2+(y2-y1)**2)**0.5)#Функція рахує відстань між точками
print(distance(x1, x2, y1, y2)) #Виводимо результат
