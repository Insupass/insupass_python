# gui.py
# Yu Gui    01/12/2017
# IsoPass commandline
# NYU CIMS

from . import hash


def run():
    # generate password by calling hash module
    # print password to shell
    def generate_pwd(*args):
        str_app_pwd = '123'
        str_master_pwd = '123'
        str_result = hash.run_hash(str_app_pwd, str_master_pwd)
        print(str_result)
        return ()
    generate_pwd()

    # TODO: write commandline mode

    return ()
