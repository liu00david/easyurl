import math
import pathlib
import json
import os
from easyurl.private.db_connector import DBConnector


def depair(z):
    """
    Inverse of Cantor pairing function
    """
    w = math.floor((math.sqrt(8 * z + 1) - 1) / 2)
    t = (w**2 + w) / 2
    y = int(z - t)
    x = int(w - y)
    return x, y


def get_shortname_tuple(index):
    """
    Given index, find shortname tuple (int,int,int,int)
    Input: index, output: tuple
    """
    I_pair = depair(index)
    A_pair = depair(I_pair[0])
    B_pair = depair(I_pair[1])
    return (A_pair[0], A_pair[1], B_pair[0], B_pair[1])


def get_shortname_string(shortname_tuple):
    """
    Given shortname_tuple, give shortname string
    adj(shortname_tuple[0])
    nouns(shortname_tuple[1])
    adj(shortname_tuple[2])
    nouns(shortname_tuple[3])
    Input: tuple, output: string
    """
    nouns_wordlist_path = get_wordlist_path("nouns")
    with open(nouns_wordlist_path) as f1:
        nouns_data = json.load(f1)

    adjectives_wordlist_path = get_wordlist_path("adjectives")
    with open(adjectives_wordlist_path) as f2:
        adjectives_data = json.load(f2)

    adjective1 = adjectives_data["words"][str(shortname_tuple[0])]
    noun1 = nouns_data["words"][str(shortname_tuple[1])]
    adjective2 = adjectives_data["words"][str(shortname_tuple[2])]
    noun2 = nouns_data["words"][str(shortname_tuple[3])]

    shortname_string = adjective1 + noun1 + adjective2 + noun2
    return shortname_string


def get_wordlist_path(pos):
    """
    Get relative path of wordlist.
    """
    curdir_path = pathlib.Path(__file__).parent.resolve()
    wordlist_path = os.path.join(curdir_path, ("wordlists/" + pos + '.json'))
    return wordlist_path


class UrlDatabaseFuncs:
    """
    Insert new URL into the database. Creates an easyurl and returns it.
    """

    def __init__(self, url):
        self.pre_url = url

    def db_add_entry(self):
        """
        Opens database, gets counters and url_mapping collections,
        """

        db = DBConnector.db_connector()
        url_mapping_collection = db["urlMapping"]
        counters_collection = db["counters"]

        # Get counter value from counters, then convert to shortname string
        # Add one to get next url's counter
        try:
            next_index = counters_collection.find()[0]['seq_value'] + 1
        except IndexError:
            print("Counter not found. Initializing counter.")
            next_index = 1
        shortname_tuple = get_shortname_tuple(next_index)
        shortname_string = get_shortname_string(shortname_tuple)
        post_url = "https://easyurl.com/" + shortname_string

        query = {"pre_url": self.pre_url, "post_url": post_url}

        url_mapping_collection.insert_one(query)

        return post_url


if __name__ == "__main__":
    for i in range(100):
        print(i, get_shortname_string(get_shortname_tuple(i)))
