def deposit_sum (deposit, month, percent):
    days = month * 30.5
    final_sum = (deposit * percent * days / 36500) + deposit
    return (final_sum)
print(deposit_sum(100_000, 6, 10))

