class UrlDatabaseFuncs:
    """
    NEED ANOTHER MODULE FOR UPDATING THE WORDS DATABASE

    Called when new URL needs a shortname.

    DATABASE STRUCT
    key:value
    index:URL or none
    Initialize with 100999999 vals
    Calls database
    Finds first 100 null indices
    Randomly picks one index, put URL in
    """

    def __init__(self):
        self.random = "hi"

    def printthis(self):
        print('this')

    def create_table(self):
        """
        creates the table?
        """

    def get_indices_database(self):
        """
        Gets 100 indices of null spaces
        """

    def add_url_database(self):
        """
        Adds URL to one of the indices
        """

    def get_shortname(self, index):
        """
        Gets shortname from index e.g. 100100100 -> cat eats here
        needs to query wordsDB
        """
