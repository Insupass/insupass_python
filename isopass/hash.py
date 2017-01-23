# hash.py
# hashing function of IsoPass
# Yu Gui   01/12/2017
# NYU CIMS

# imports
import sys
import math
import hashlib

# global vars
_ip_debug = True


# func: hash data with sha512 algorithm
# @tested python3.5
def hash_sha512(str_byte_message):
    return hashlib.sha512(str_byte_message).hexdigest().lower()


# func: hash data with sha256 algorithm
# @tested python3.5
def hash_sha256(str_byte_message):
    return hashlib.sha256(str_byte_message).hexdigest().lower()


# TODO:transpose
# func: transpose by hex blocks
def transpose(str_input):

    return str_input


# TODO:expansion function
# func: expand by hex blocks
def expand(str_input, i_target_len):

    return str_input


# func: encode binary data with base 58 encoding.
# base 58 encoding is widely used in Bitcoin address encoding
# and is a very concise and unambiguous encoding procedure
# @tested python3.5
def base58_encode(str_input):
    __str_code = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    i_code = int(str_input, 16)

    if _ip_debug:
        print('base 58 encoding: ')
        print('b16: ', str_input)
        print('b10: ', i_code)

    str_return = ""
    while i_code > 0:
        i_code, i_remainder = divmod(i_code, 58)
        str_return += __str_code[i_remainder]

    # reverse results of divmod
    str_temp = str_return[::-1]
    str_return = str_temp

    if _ip_debug:
        print('b58: ', str_return)

    return str_return


# func: main hashing function
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

    # TODO: create unit tests

    str_seed1 = args[0]
    str_seed2 = args[1]

    str_input = str_seed1 + str_seed2
    str_result = str_input

    # define hashing algorithms
    for algo in l_argv_algo:
        # standard message digest algos
        if algo == "sha512":
            str_input = str_result
            str_result = hash_sha512(str_input.encode())

            if _ip_debug:
                print('sha512: ', str_result)

        if algo == "sha256":
            str_input = str_result
            str_result = hash_sha256(str_input.encode())

            if _ip_debug:
                print('sha256: ', str_result)

        # transpose
        if algo == "t" or algo == "transpose":
            str_input = str_result
            str_result = transpose(str_input)

            if _ip_debug:
                print('transpose: ', str_result)

        # expansion
        try:
            if algo[0] == "e":
                i_target_len = int(algo[1:])
                str_input = str_result
                str_result = expand(str_input, i_target_len)

                if _ip_debug:
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

    print('Digest: ', str_result)
    print('Length: ', len(str_result))
    print('\n')

    return str_result


