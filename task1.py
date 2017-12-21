numbers = [float(i) for i in input().split()]


def second_max_number(numbers):
    """
    Ця функція повертає другий максимальний елемент
    Args:
        numbers: список
    Returns: дійсне числa
    Exampples:
        >>> print(sum_sequence([1 2 3 4 5 6 7 8 9]))
        8
        >>> print(sum_sequence([1 2 3 4 5 j 7 8 9]))
        File "C:/Users/User/Desktop/Python/12/task1.py",
        line 1, in <listcomp>
        numbers = [float(i) for i in input().split()]
        ValueError: could not convert string to float: 'f'
    """
    numbers.remove(min(numbers))
    if len(numbers) == 2:
        return int(min(numbers))
    else:
        return(second_max_number(numbers))
print(second_max_number(numbers))
