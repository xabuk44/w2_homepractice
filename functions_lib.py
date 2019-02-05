def deposit_sum (deposit, month, percent):
    days = month * 30.5
    final_sum = (deposit * percent * days / 36500) + deposit
    return (final_sum)


def vat (s):
    vat_rus = s * 20 / 100.
    return vat_rus
