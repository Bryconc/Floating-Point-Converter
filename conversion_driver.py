__author__ = 'Brycon'

import decimal_to_float_conv
import float_to_decimal_conv

INPUT = '-267.0' #Only input as decimal or binary

SIGN_BIT_SIZE = 1
EXPONENT_BIT_SIZE = 5
MANTISSA_SIZE = 10
BIT_LENGTH = SIGN_BIT_SIZE + EXPONENT_BIT_SIZE + MANTISSA_SIZE


def main():
    float_to_decimal_conv.set_const_values(SIGN_BIT_SIZE, EXPONENT_BIT_SIZE, MANTISSA_SIZE)
    decimal_to_float_conv.set_const_values(SIGN_BIT_SIZE, EXPONENT_BIT_SIZE, MANTISSA_SIZE)
    if is_binary(INPUT):
        answer = float_to_decimal_conv.intr_float(INPUT)
        print(INPUT + " as a decimal is: " + str(answer))
    else:
        answer = decimal_to_float_conv.conv_decimal(INPUT)
        print("%s as a(n) %d-bit floating point number: %s (%s)" %
              (INPUT, BIT_LENGTH, answer, hex(int(answer, 2))))

    try:
        check_answer(INPUT, answer)
    except:
        import sys
        print("Possible precision loss error. Be advised.", file=sys.stderr)


def check_answer(inp, answer):
    if is_binary(inp):
        checked_answer = decimal_to_float_conv.conv_decimal(answer)
        #print("Input: %s (%s) Checked Answer: %s (%s)" % (str(inp), type(inp), str(checked_answer), type(checked_answer)))
        assert checked_answer == inp
    else:
        checked_answer = float_to_decimal_conv.intr_float(answer)
        print("Input: %s (%s) Checked Answer: %s (%s)" % (str(inp), type(inp), str(checked_answer), type(checked_answer)))
        assert str(checked_answer) == inp


def is_binary(num_str):
    for c in num_str:
        if c != '0' and c != '1':
            return False
    return True

if __name__ == '__main__':
    main()