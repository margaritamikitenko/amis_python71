elements = [float(i) for i in input().split()]
el1 = elements


def max_el(elements):
    """
    Ця функція повертає кількість елементів,
    що дорінюють максимальному елементу
    Args:
        numbers: список
    Returns: дійсне числa
    Exampples:
        >>> print(sum_sequence(2 3 4 7 4 7 7 4))
        3
        >>> print(sum_sequence(1 3 4 7 а 7 7 4))
        File "C:/Users/User/Desktop/Python/12/task2.py",
        line 1, in <listcomp>
        elements = [float(i) for i in input().split()]
        ValueError: could not convert string to float: 'а'
    """
    if len(elements) == 0:
        return '0'
    else:
        if len(elements) > 1:
            if elements[0] > elements[1]:
                del elements[1]
                return max_el(elements)
            else:
                return max_el(elements[1:])
        elif len(elements) == 1:
            return el1.count(elements[0])

print(max_el(elements))
