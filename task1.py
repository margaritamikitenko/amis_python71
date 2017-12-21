x = float(input())
n = int(input())

while (x == 1):
    x = float(input('Ви ввели некоректне значення х, спробуйте ще раз: '))
else:
    x = float(x)


def sum_sequence(x,n): #функція обчислює загальну суму послідовності
    if 1 < n:
        t = ((2 * x + 1) ** n)/(x - 1)
        return (t + sum_sequence(x,n-1))
    elif n == 1:
        return ((2 * x + 1) ** n)/(x - 1)

def test_one_digit():
    assert(sum_sequence(3,4)==1400.0)
    assert(sum_sequence(-3,4)== -130.0)
    assert(sum_sequence(0.3,5)== -36.13622857142858)
    print('Все вірно')
        
test_one_digit()
print(sum_sequence(x,n))
