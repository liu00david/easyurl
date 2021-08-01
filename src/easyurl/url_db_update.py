import math
import pathlib
import json
import os
from pymongo import MongoClient

cluster = MongoClient("test")

def pair(k1, k2):
    """
    Cantor pairing function
    """
    z = int(0.5 * (k1 + k2) * (k1 + k2 + 1) + k2)
    return z


def depair(z):
    """
    Inverse of Cantor pairing function
    """
    w = math.floor((math.sqrt(8 * z + 1) - 1) / 2)
    t = (w**2 + w) / 2
    y = int(z - t)
    x = int(w - y)
    return x, y


def get_wordlist_path(pos):
    curdir_path = pathlib.Path(__file__).parent.resolve()
    wordlist_path = os.path.join(curdir_path, ("wordlists/" + pos + '.json'))
    return wordlist_path


class UrlDatabaseFuncs:
    """
    Called when new URL needs a shortname.
    """

    def __init__(self, url):
        self.url = url

        i = 0
        while i < 100000:
            shortname_tuple = self.get_shortname_tuple(i)
            shortname_string = self.get_shortname_string(shortname_tuple)
            print("easyurl.com/" + shortname_string)
            i += 1


    def db_get_index(self):
        """
        Gets next avail index in DB
        Input: none, output: index
        """

    def get_shortname_tuple(self, index):
        """
        Given index, find shortname tuple (int,int,int,int)
        Input: index, output: tuple
        """
        I_pair = depair(index)
        A_pair = depair(I_pair[0])
        B_pair = depair(I_pair[1])
        return (A_pair[0], A_pair[1], B_pair[0], B_pair[1])

    def get_shortname_string(self, shortname_tuple):
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


    def db_add_entry(self, index, url):
        """
        Given index, url, entry into DB
        Input: self index, output: none
        """
