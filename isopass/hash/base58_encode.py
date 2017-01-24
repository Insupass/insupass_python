# Encode Hex string to Base 58 encoding
# Yu Gui    1/24/2017
# base 58 encoding is widely used in Bitcoin address encoding
# and is a very concise and unambiguous encoding procedure
# @tested python3.5


def base58_encode(str_input):
    __str_code = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    i_code = int(str_input, 16)

    if __debug__:
        print('base 58 encoding: ')
        print('b16: ', str_input)
        print('b10: ', i_code)

    str_return = ""
    while i_code > 0:
        i_code, i_remainder = divmod(i_code, 58)
        str_return += __str_code[i_remainder]

    # reverse results of floor division to obtain final string
    str_temp = str_return[::-1]
    str_return = str_temp

    if __debug__:
        print('b58: ', str_return)

    return str_return
