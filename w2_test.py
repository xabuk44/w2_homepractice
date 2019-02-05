def deposit_sum (deposit, month, percent):
    """
    >>> deposit_sum(100_000, 6, 10) #doctest: +ELLIPSIS
    105013.69...
    >>> deposit_sum(200_000, 12, 8.7)#doctest: +ELLIPSIS
    217447.67...
    """
    days = month * 30.5
    final_sum = (deposit * percent * days / 36500) + deposit
    return (final_sum)
print(deposit_sum(200_000, 12, 8.7))
print(deposit_sum(100_000, 6, 10))