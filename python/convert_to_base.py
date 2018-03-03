def int_to_base(num, base):
    # Converts a non-negative integer to an arbitrary base
    # Returns an array, e.g. int_to_base(6, 2) => [1, 1, 0]
    if num == 0:
        return []
    quotient = num // base # Integer division
    remainder = num % base
    # (Fill in the missing line here)
    return int_to_base(quotient,base) + [remainder]


print [2] + [2] +[4]

print int_to_base(15,10)
