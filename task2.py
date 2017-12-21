elements = [float(i) for i in input().split]

def min_number(elements):
    """
    Ця функція повертає найменший елемент зі списку elemtnts
    Args:
        elemtns: список
    Returns:
        elements: дійсне число
    Examples:
        >>>print(sum_sequence([4, 6, 7, 3, 9, 9, 0, 0))
        0.0
        >>>print(sum_sequence([6, 0, 0, f] ))
        Traceback (most recent call last):
        File "C:/Users/User/Desktop/Python/11/task2(11).py",
        line 1, in <listcomp>
        elemеnts = [float(i) for i in input().split()]
        ValueError: could not convert string to float: 'f'
    """
    if len(elements) != 1: 
        if elements[0] >= elements[1]:
            return min_number(elements[1:])
        else:
            del elements[1]
            return min_number(elements)
    else:
        return elements[0]

print(min_number(elements))

