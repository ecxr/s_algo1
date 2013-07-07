def merge(x, y):
    """
    Input: 2 sorted lists
    Output: a single combined sorted list

    >>> merge([1,3,5], [2,4,6])
    [1, 2, 3, 4, 5, 6]
    """
    k = len(x)
    l = len(y)
    if (k == 0): 
        return y
    if (l == 0): 
        return x
    if x[0] <= y[0]:
        return [x[0]] + merge(x[1:k], y[0:l])
    else:
        return [y[0]] + merge(x[0:k], y[1:l])

def mergesort(L):
    """
    Input: A list of numbers L[0..n-1]
    Output: A sorted version of this list

    >>> mergesort([2,4,3,6,1,5])
    [1, 2, 3, 4, 5, 6]
    """
    n = len(L)
    mid = n//2
    if n > 1:
        return merge(mergesort(L[0:mid]),
                     mergesort(L[mid:n]))
    else:
        return L

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    print("Tests done")
