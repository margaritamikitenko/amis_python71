a = float(input())
n = int(input()) #Вводимо числа

def power(a, n):
    if n == 0:
        return 1
    else:
        return a*power(a, n-1) #Функція обчислює значення
print(power(a, n)) #Виводимо результат
