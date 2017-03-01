# Hash package __init__.py
# Yu Gui    1/24/2017

from .sha512 import hash_sha512
from .expand import expand
from .transpose import transpose
from .base58_encode import base58_encode
from .trim_str import trim_str

import sys


# main hashing function
def run_hash(*args):
    # receive hashing scheme
    l_argv = sys.argv
    try:
        str_argv_scheme = l_argv[1]
    except IndexError:
        str_argv_scheme = "sha512-sha512-b58"

    l_argv_scheme = str_argv_scheme.split("-")
    l_argv_algo = l_argv_scheme[:-1]
    l_argv_encode = l_argv_scheme[-1:]
    print('Hashing algorithms: ', l_argv_algo)
    print('Encoding: ', l_argv_encode)

    str_seed1 = args[0]
    str_seed2 = args[1]

    str_input = str_seed1 + str_seed2
    str_result = str_input

    # parsing hash parameters
    for algo in l_argv_algo:
        # standard message digest algo(s)
        if algo == "sha512":
            str_input = str_result
            str_result = hash_sha512(str_input.encode())

            if __debug__:
                print('sha512: ', str_result)

        # transpose
        if algo == "t" or algo == "transpose":
            str_input = str_result
            str_result = transpose(str_input)

            if __debug__:
                print('transpose: ', str_result)

        # expansion
        try:
            if algo[0] == "e":
                i_target_len = int(algo[1:])
                str_input = str_result
                str_result = expand(str_input, i_target_len)

                if __debug__:
                    print('expansion: ', str_result)

        except IndexError:
            pass

    # define encode algorithms
    for encode_algo in l_argv_encode:
        # ASCII string encoding
        if encode_algo == "hstr":
            # do nothing
            pass

        # base 58 encoding
        if encode_algo == "b58":
            str_input = str_result
            str_result = base58_encode(str_input)

    # trim string to specified length
    str_result = trim_str(str_result, 12)

    print('Digest: ', str_result)
    print('Length: ', len(str_result))
    print('\n')

    return str_result
