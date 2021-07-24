class UrlDatabaseFuncs:
    """
    NEED ANOTHER MODULE FOR UPDATING THE WORDS DATABASE

    Called when new URL needs a shortname.

    DATABASE STRUCT
    2 tables, one of urlindex:url, another that keeps tracks of taken indices
    Calls database

    Randomly picks one index, put URL in
    """

    def __init__(self):
        self.random = "hi"

    def printthis(self):
        print('this')

    def create_table(self):
        """
        creates the table
        """

    def get_indices_database(self):
        """
        Gets first 100 null values' indices
        """

    def add_url_database(self):
        """
        Adds URL to one of the indices
        """

    def get_shortname(self, index):
        """
        Gets shortname from index e.g. 100111000 -> cat eats here
        needs to query wordsDB
        adjectives(100)
        nouns(111)
        verbs(000)

        """
