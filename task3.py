elements = [int(i) for i in input().split()]

def groups_find(elements,i,ter,k):
    """
    Ця функця повертає найбільшу кількість елементів,
    що стоять поряд у списку
    Args:
        elements: список натуральних чисел
        i:  чило
        ter:  чило
        k: число
    Returns:
        натуральне число
    Examples:
        >>> print(1 2 3 4 4 4 5 6 1 1 1 1 3))
        4
    """
    
    if i < len(elements)-1 and elements[i] == elements[i+1]:
        k += 1
            
        return groups_find(elements,i+1,ter,k)
    else :
        return k,ter

def quantity(elements,i,max_k):
    
    if i < len(elements):
        d = groups_find(elements,i,0,1)
        if max_k < d[0]:
            max_k = d[0]
        return quantity(elements,i+1,max_k)
    else:
        return max_k
            


a = [1,2,3,3,3,3,3,6,6,6,6,6,6,6] 
print(quantity(elements, 0, 0))
