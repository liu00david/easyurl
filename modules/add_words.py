import json
import os


class UrlLogic:
    """
    takes inn part of speech (noun,adjective,adverb) and writes into files
    """

    def __init__(self, POS):
        self.POS = POS

        cur_dir = os.path.dirname(__file__)
        POS_json = os.path.join(cur_dir, '/wordlists/' + POS + 's.json')
        try:
            with open(POS_json) as filename:
                self.word_dict = json.load(filename)
        except Exception:
            print("wordlist (" + POS_json + ") not found.")

