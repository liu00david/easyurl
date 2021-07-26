import argparse

from easyurl.wordlist_db_update import WordlistDatabaseFuncs

def start_wordlist(args):
    action = args.action
    pos = args.pos

    word = "" if action == "reset" else input("word:\n")

    WordlistDatabaseFuncs(action, pos, word)


def main():
    parser = argparse.ArgumentParser(description='Update wordlist DB.')
    parser.add_argument('action', type=str, choices=["add","replace","reset"],
                        help='Choose the action.')
    parser.add_argument('pos', type=str, choices=["nouns","adjectives"],
                        help='Choose the part of speech.')

    args = parser.parse_args()

    start_wordlist(args)


if __name__ == '__main__':
    main()
