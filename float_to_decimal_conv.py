__author__ = 'Brycon'

SIGN_BIT_SIZE = -1
EXPONENT_BIT_SIZE = -1
OFFSET = -1
MANTISSA_SIZE = -1

def set_const_values(sign, exponent, mantissa):
    global SIGN_BIT_SIZE, EXPONENT_BIT_SIZE, OFFSET, MANTISSA_SIZE

    SIGN_BIT_SIZE = sign
    EXPONENT_BIT_SIZE = exponent
    OFFSET = (2 ** (EXPONENT_BIT_SIZE - 1)) - 1
    MANTISSA_SIZE = mantissa


def move_decimal_fl(mantissa, exp):
    #print(mantissa)
    if exp < 0:
        while exp < 0:
            idx = mantissa.index(".")
            if idx > 0:
                mantissa = mantissa[: idx - 1] + '.' + mantissa[idx - 1] + mantissa[idx + 1:]
            else:
                mantissa = '.0' + mantissa[idx + 1:]
            exp += 1
            #print(mantissa)

    elif exp > 0:
        while exp > 0:
            idx = mantissa.index(".")
            if idx == len(mantissa) - 1:
                mantissa = mantissa[:idx] + '0.'
            else:
                mantissa = mantissa[:idx] + mantissa[idx + 1] + "." + mantissa[idx + 2:]
            exp -= 1
            #print(mantissa)

    return mantissa


def intr_float(input):
    sign_bit = int(input[0:SIGN_BIT_SIZE], 2)
    sign = 1 if sign_bit == 0 else -1

    exponent = int(input[SIGN_BIT_SIZE: EXPONENT_BIT_SIZE + SIGN_BIT_SIZE], 2) - OFFSET
    mantissa = '1.' + input[EXPONENT_BIT_SIZE + SIGN_BIT_SIZE: ]
    str = move_decimal_fl(mantissa, exponent)
    idx = str.index('.')
    return sign * (intr_whole(str[:idx]) + intr_decimal(str[idx + 1:]))


def intr_whole(whole):
    if whole == '':
        return 0
    return int(whole, 2)


def intr_decimal(decimal):
    sum = 0
    n = 1
    for x in decimal:
        sum += int(x) * (2 ** -n)
        #print("For %x sum is %f. n = %d" % (int(x), sum, n))
        n += 1
    return sum