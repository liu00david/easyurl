from easyurl.wordlist_db_update import WordlistDatabaseFuncs


def main():

    reset = True

    action = input("action:\n")
    part_of_speech = input("part of speech:\n")
    word = ""
    if not reset:
        word = input("word:\n")
    WordlistDatabaseFuncs(action, part_of_speech, word)


if __name__ == '__main__':
    main()
