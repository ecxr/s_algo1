import sys
import random

def count_and_merge(left,right):
    """
    Input: left and right are sorted lists.
    Output: a new sorted list containing the same elements
    as (left + right) would contain.

    >>> count_and_merge([1,3,5], [2,4,6])
    (3, [1, 2, 3, 4, 5, 6])
    """
    result = []
    i,j = 0, 0
    count = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
            count += len(left[i:])
    while (i < len(left)):
        result.append(left[i])
        i = i + 1
    while (j < len(right)):
        result.append(right[j])
        j = j + 1
    return (count, result)

def sort_count_inversions(L):
    """
    Input: A list of numbers L[0..n-1]
    Output: A sorted version of this list

    >>> sort_count_inversions([1,3,5,2,4,6])
    (3, [1, 2, 3, 4, 5, 6])
    """
    x, y, z = 0, 0, 0
    if len(L) < 2:
        return 0, L[:]
    else:
        middle = len(L) // 2
        (x, left) = sort_count_inversions(L[:middle])
        (y, right) = sort_count_inversions(L[middle:])
        (z, together) = count_and_merge(left,right)
        return (x+y+z, together)

def brute_force_inversions(a):
    """ Brute force algorithm to count number of inversions in a list a"""
    no_of_inversions=0
    for i in range(len(a)):
        for j in range(i+1,len(a)):
            if a[i] > a[j]:
                no_of_inversions+=1
    return no_of_inversions

def generate_test_cases(n,m):
    """ Generates and return an random array of n lists each of size m"""
    test_cases=[]
    for i in range(n):
        test_case=[]
        for j in range(m):
            test_case.append(random.randint(1,n))
        test_cases.append(test_case)
    return test_cases

def test_algorithms(n,m):
    """ 
    Tests the correctness of the devised algorithm for n test cases 
    each of length m
    """
    l=generate_test_cases(n,m)
    failed_test_cases=[]
    flag=True
    for item in l:
        count_brute_force_inversions = brute_force_inversions(item)
        temp,count_algorithm_inversions = sort_count_inversions(item)
        if count_brute_force_inversions != count_algorithm_inversions:
            flag=False
            failed_test_cases.append(item)
    if flag:
        print("All Test Cases Passed")
    else:
        print("Some Test Cases Failed")
        print("List of failed test cases are: ")
        print(failed_test_cases)

def doTests():
    num, a = sort_count_inversions([1,3,5,2,4,6])
    print(num, a)
    num, a = sort_count_inversions([1,5,3,2,4])
    print(num, a)
    num, a = sort_count_inversions([5,4,3,2,1])
    print(num, a)
    num, a = sort_count_inversions([1,6,3,2,4,5])
    print(num, a)
    test_algorithms(100, 100)

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    #doTests()
    f = open('IntegerArray.txt', 'r')
    a = [int(l.strip('\n')) for l in f.readlines()]
    (count, sorted_a) = sort_count_inversions(a)
    #print(sorted_a)
    print(count)
    #print(brute_force_inversions(a))



