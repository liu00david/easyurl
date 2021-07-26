import json
import os
import pathlib
import re


class WordlistDatabaseFuncs:
    """
    Updates the wordlists DB
    """

    def __init__(self, action, part_of_speech, word):
        self.word = word
        self.pos = part_of_speech

        if action == "add":
            if self.check_word_format() == False:
                print("Word formatting failed.")
                exit()
            self.add_word()
        elif action == "remove":
            self.remove_word()
        else:
            self.reset()


    def get_json_data(pos):
        curdir_path = pathlib.Path(__file__).parent.resolve()
        wordlist_path = os.path.join(curdir_path, ("wordlists/" + pos + '.json'))
        with open(wordlist_path) as f:
            data = json.load(f)
        return data


    def check_word_format(self):
        """
        Only returns True if word is
        1-5 letters long
        have only letters (a-z A-Z)
        Cleans the word to lowercase
        """
        word = self.word
        pattern = re.compile("[A-Za-z]+")
        if not(1 <= len(word) <= 5):
            print("Word must be 1-5 letters long.")
            return False
        if not(pattern.fullmatch(word)):
            print("Word must be only letters (a-z, A-Z)")
            return False
        # lowercase the word
        self.word = word.lower()
        return True


    def add_word(self):
        """
        Adds word to partsofspeech jsons.
        If exists already, do nothing.
        """
        word = self.word    # easier to call

        data = self.get_json_data(self.pos)

        # checking if word exists, or just has 's' added
        existing_words = data["words"].values()
        word_with_s = word + "s"
        word_without_s = word[0:-1] if word[-1] == 's' else word
        if word_with_s in existing_words or word_without_s in existing_words:
            print("Already exists (or just has an 's')! Nothing done.")
            return

        next_index = int(data["cur_index"]) + 1     # new index
        data["words"][next_index] = word       # update wordlist
        data["words"] = dict(sorted(data["words"].items(), key=lambda item: item[1])) # alphabetisize
        data["cur_index"] = next_index              # update index

        with open(wordlist_path, 'w') as f:
            json.dump(data, f, indent = 4)

        print(f"[{word}] added to [{self.pos}]. This is the [{next_index}] indexed word added.")


    def remove_word(self):
        pass


    def reset(self):
        """
        Resets data struct of the JSON.
        """
        resetdata = {
            "words" : {},
            "cur_index" : -1,
        }
        curdir_path = pathlib.Path(__file__).parent.resolve()
        wordlist_path = os.path.join(curdir_path, ("wordlists/" + self.pos + '.json'))
        with open(wordlist_path, 'w') as f:
            json.dump(resetdata, f, indent = 4)


