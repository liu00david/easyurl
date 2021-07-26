import json
import os
import pathlib
import re

def check_word_format(word):
    """
    Only returns True if word is
    1-5 letters long
    have only letters (a-z)
    Cleans the word to lowercase
    """
    pattern = re.compile("[a-z]+")
    if not(1 <= len(word) <= 5):
        print("BAD FORMAT: Word must be 1-5 letters long.")
        return False
    if not(pattern.fullmatch(word)):
        print("BAD FORMAT: Word must be only letters (a-z, A-Z)")
        return False
    return True


def exists_already(data, word):
    # checking if word exists, or just has 's' added
    existing_words = data["words"].values()
    word_with_s = word + "s"
    word_without_s = word[0:-1] if word[-1] == 's' else word
    if word_with_s in existing_words or word_without_s in existing_words:
        print("Already exists (or just has an 's')! Nothing done.")
        return True
    return False


class WordlistDatabaseFuncs:
    """
    Updates the wordlists DB
    """

    def __init__(self, action, pos, word):
        self.word = word.lower()
        self.pos = pos

        if action == "add":
            if not check_word_format(self.word):
                exit()
            self.add_word()
        elif action == "replace":
            self.replace_word()
        else:
            self.reset()

    def get_wordlist_path(self):
        curdir_path = pathlib.Path(__file__).parent.resolve()
        wordlist_path = os.path.join(curdir_path, ("wordlists/" + self.pos + '.json'))
        return wordlist_path


    def add_word(self):
        """
        Adds word to partsofspeech jsons.
        If exists already, do nothing.
        """
        word = self.word    # easier to call word now

        wordlist_path = self.get_wordlist_path()
        with open(wordlist_path) as f:
            data = json.load(f)

        if exists_already(data,word):
            exit()

        next_index = int(data["cur_index"]) + 1     # new index
        data["words"][next_index] = word            # update wordlist
        data["words"] = dict(sorted(data["words"].items(), key=lambda item: item[1])) # alphabetisize
        data["cur_index"] = next_index              # update index

        with open(wordlist_path, 'w') as f:
            json.dump(data, f, indent = 4)

        print(f"[{word}] added to [{self.pos}]. This is the [{next_index}] indexed word added.")


    def replace_word(self):
        """
        Replaces the word in the wordlist if it exists.
        Also checks new word for formatting.
        """
        wordlist_path = self.get_wordlist_path()
        with open(wordlist_path) as f:
            data = json.load(f)

        for index, exist_word in data["words"].items():
            if self.word == exist_word:
                new_word = input("New word:\n")
                if not check_word_format(new_word):
                    exit()
                if exists_already(data,new_word):
                    exit()
                # write new_word in
                data["words"][index] = new_word
                data["words"] = dict(sorted(data["words"].items(), key=lambda item: item[1]))

                with open(wordlist_path, 'w') as f:
                    json.dump(data, f, indent = 4)
                print(f"[{self.word}] has been replaced by [{new_word}]!")
                return

        print(f"[{self.word}] does not exist in list!")


    def reset(self):
        """
        Resets data struct of the JSON.
        """
        resetdata = {
            "words" : {},
            "cur_index" : -1,
        }
        wordlist_path = self.get_wordlist_path()
        with open(wordlist_path, 'w') as f:
            json.dump(resetdata, f, indent = 4)
        print(f"[{self.pos}] wordlist has been reset.")


