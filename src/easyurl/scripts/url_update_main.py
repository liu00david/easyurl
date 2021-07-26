import argparse

from easyurl.url_db_update import UrlDatabaseFuncs


def start_url(args):
    """
    12,753,774 is the max depair input index for 99,99 nouns and adjs
    pair(0,5049)
    Say that theres a cap of 12,000,000

    """
    UrlDatabaseFuncs("hi.com")

def main():
    parser = argparse.ArgumentParser(description='Update wordlist DB.')
    # parser.add_argument('action', type=str, choices=["add","replace","reset"],
    #                     help='Choose the action.')
    # parser.add_argument('pos', type=str, choices=["nouns","adjectives"],
    #                     help='Choose the part of speech.')

    args = parser.parse_args()

    start_url(args)

if __name__ == '__main__':
    main()
