""" The main script called from the command line to create a backronym.

Credit:
Will Roper: w.roper@sussex.ac.uk
Jussi K. Kuusisto: J.Kuusisto@sussex.ac.uk
"""
import sys


def main():
    """ Main function called from the command line.

        Takes input from the command line as a list of arguments and finds
        the optimal backronym based on the bag of keys words and desired
        acronym.

    :return:
    """

    # Get acronym and bag of words
    acronym = sys.argv[1]
    bag_of_words = sys.argv[2:]

    # MAIGC
    backronym = "profit"

    print("Backronym: %s" % backronym)
