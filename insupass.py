# Yu Gui   04/27/2016
# Insupass

import math
import hashlib
import sys


# hash data with sha512 algorithm
def hash_sha512(s_byte_message):
    return hashlib.sha512(s_byte_message).hexdigest().lower()


# hash data with sha384 algorithm
def hash_sha384(s_byte_message):
    return hashlib.sha384(s_byte_message).hexdigest().lower()


# hash data with sha256 algorithm
def hash_sha256(s_byte_message):
    return hashlib.sha256(s_byte_message).hexdigest().lower()


# hash data with sha1 algorithm
def hash_sha1(s_byte_message):
    return hashlib.sha1(s_byte_message).hexdigest().lower()


# hash data with md5 algorithm
def hash_md5(s_byte_message):
    return hashlib.md5(s_byte_message).hexdigest().lower()


# encode binary data with base 58 encoding
def base58_encode(s_input):
    __s_code = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
    i_code = int(s_input, 16)
    # print(i_code)

    s_return = ""
    while (i_code > 0):
        i_code, i_remainder = divmod(i_code, 58)
        s_return += __s_code[i_remainder]
    s_temp = s_return[::-1]
    s_return = s_temp

    return s_return


# TODO:transpose
# transpose by hex blocks
def transpose(s_input):

    return s_input


# expand by hex blocks
def expand(s_input, i_target_len):

    return s_input


# main function
def __yg_main():
    # receive hashing scheme
    l_argv = sys.argv
    try:
        s_argv_scheme = l_argv[1]
    except IndexError:
        s_argv_scheme = "s25-s25-b58"

    l_argv_scheme = s_argv_scheme.split("-")
    l_argv_algo = l_argv_scheme[:-1]
    l_argv_encode = l_argv_scheme[-1:]
    print("Hashing algorithms: ", l_argv_algo)
    print("Encoding: ", l_argv_encode)

    # TODO: change test case back
    # receive seeds
    # s_seed1 = "12"
    # s_seed2 = "34"
    s_seed1 = str(input("Please input seed1: \n"))
    s_seed2 = str(input("please input seed2: \n"))
    s_input = s_seed1 + s_seed2
    s_result = s_input

    # define hashing algorithms
    for algo in l_argv_algo:
        # standard message digest algos
        if algo == "s25" or algo == "sha512":
            s_input = s_result
            s_result = hash_sha512(s_input.encode())

        if algo == "s23" or algo == "sha384":
            s_input = s_result
            s_result = hash_sha384(s_input.encode())

        if algo == "s22" or algo == "sha256":
            s_input = s_result
            s_result = hash_sha256(s_input.encode())

        if algo == "s1" or algo == "sha1":
            s_input = s_result
            s_result = hash_sha1(s_input.encode())

        if algo == "m5" or algo == "md5":
            s_input = s_result
            s_result = hash_md5(s_input.encode())

        # transpose
        if algo == "t" or algo == "transpose":
            s_input = s_result
            s_result = transpose(s_input)

        # expansion
        try:
            if algo[0] == "e":
                i_target_len = int(algo[1:])
                s_input = s_result
                s_result = expand(s_input, i_target_len)

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
            s_input = s_result
            s_result = base58_encode(s_input)

    print("Length: ", len(s_result))
    print("Digest: ", s_result)


__yg_main()
