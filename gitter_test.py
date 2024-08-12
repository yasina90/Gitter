def count(x: list) -> int:
    """
    Counts the number of alphabetic characters in the given list.

    :param x: A list of characters or strings.
    :type x: list
    :return: The count of alphabetic characters in the list.
    :rtype: int
    """
    count = 0
    for i in x:
        if i.isalpha():
            count += 1
    return count
