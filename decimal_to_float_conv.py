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


def move_decimal_dec(str):
    #print(str)
    idx = str.index('.')
    int_value = int(str[:idx], 2)
    exponent = 0

    if int_value > 1:
        while int_value > 1:
            idx = str.index('.')
            str = str[:idx - 1] + "." + str[idx - 1] + str[idx + 1:]
            exponent += 1
            idx -= 1
            int_value = int(str[:idx], 2)
            #print(str)
    else:
        while int_value < 1:
            idx = str.index('.')
            str = str[:idx] + str[idx + 1] + "." + str[idx + 2:]
            exponent -= 1
            idx += 1
            int_value = int(str[:idx], 2)
            #print(str)

    return str, exponent


def conv_whole(str):
    return bin(int(str))[2:]


def conv_fract(str):
    n = 0
    build_str = ''
    fract = float('.' + str)

    while n < MANTISSA_SIZE * 2:
        fract *= 2
        if fract >= 1:
            build_str += '1'
            fract -= 1
        else:
            build_str += '0'
        n += 1

    return build_str


def strip_sign(str):
    if str[0] == '-':
        return '1', str[1:]
    else:
        return '0', str


def conv_decimal(con_str):
    sign, con_str = strip_sign(str(con_str))
    idx = con_str.index('.')
    whole = conv_whole(con_str[:idx])
    fract = conv_fract(con_str[idx + 1:])
    con_str = whole + '.' + fract
    con_str, exponent = move_decimal_dec(con_str)
    idx = con_str.index('.')

    mantissa = con_str[idx + 1: idx + 1 + MANTISSA_SIZE]
    exponent = bin(exponent + OFFSET)[2:].zfill(EXPONENT_BIT_SIZE)

    #print("Sign: %s Exp: %s Mantissa: %s" % (sign, exponent, mantissa))

    return sign + exponent + mantissa