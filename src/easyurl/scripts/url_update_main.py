import argparse

from easyurl.url_db_update import UrlDatabaseFuncs


def start_url_update(args):
    verbose = args.verbose
    """
    12,753,774 is the max depair input index for 99,99 nouns and adjs
    pair(0,5049)
    Say that theres a cap of 12,000,000

    """
    urlUpdater = UrlDatabaseFuncs("hi.com")
    post_url = urlUpdater.db_add_entry()
    if verbose:
        print(post_url)


def main():
    parser = argparse.ArgumentParser(description='Update wordlist DB.')
    parser.add_argument('-v', '--verbose', default=False, action='store_true',
                        help='Show verbose. Default show nothing.')

    args = parser.parse_args()

    start_url_update(args)


if __name__ == '__main__':
    main()
