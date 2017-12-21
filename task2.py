a, n = float(input()), int(input())#Вводимо числа

def power(a,n):
    if n == 0:
        return 1
    elif n > 0:
        return a*power(a, n-1)
    else:
        return 1/a*power(a, n+1)#функція рахує а^n

print(power(a, n))#Виводимо результат
