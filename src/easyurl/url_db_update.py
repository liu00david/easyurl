import math


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


class UrlDatabaseFuncs:
    """
    Called when new URL needs a shortname.
    """

    def __init__(self):
        self.url = "hi.com"

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
        out_pair = depair(index)
        in_pair_A = depair(out_pair[0])
        in_pair_B = depair(out_pair[1])
        return tuple(in_pair_A[0], in_pair_A[1], in_pair_B[0], in_pair_B[1])

    def get_shortname_string(self, shortname_tuple):
        """
        Given shortname_tuple, give shortname string
        adj(shortname_tuple[0])
        nouns(shortname_tuple[1])
        adj(shortname_tuple[2])
        nouns(shortname_tuple[3])
        Input: tuple, output: string
        """

    def db_add_entry(self, index, url):
        """
        Given index, url, entry into DB
        Input: self index, output: none
        """
