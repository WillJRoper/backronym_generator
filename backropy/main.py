""" The main script called from the command line to create a backronym.

Credit:
Will Roper: w.roper@sussex.ac.uk
Jussi K. Kuusisto: J.Kuusisto@sussex.ac.uk
"""
from nltk.corpus import wordnet
import nltk.corpus
import sys
import nltk
import random


def backronym_loop(acronym, words):
    output = ''
    random.shuffle(words)
    for letter in acronym:
        for j, word in enumerate(words):
            if letter.lower() in word.lower():
                output += word.lower().replace(letter, letter.upper(), 1)+' '
                words.pop(j)
                break

    return output.strip()


def main():
    """ Main function called from the command line.

        Takes input from the command line as a list of arguments and finds
        the optimal backronym based on the bag of keys words and desired
        acronym.

    :return:
    """

    # Check we have the necessary NLTK resources
    nltk.download('wordnet')

    # Get acronym and bag of words
    n_results = int(sys.argv[1])
    acronym = sys.argv[2].lower()
    bag_of_words = sys.argv[3:]

    # Include some stop words that could be useful
    bag_of_words.extend(["the", "and", "is", "of", "in", "for",
                         "from", "or", "a", "an", "by"])

    # Set up list for the synonyms
    synonyms = []

    # Expand the bag of words with synonyms
    for word in bag_of_words:  # loop over the bag of words

        # Loop over synonyms for this word
        for syn in wordnet.synsets(word):
            for i in syn.lemmas():
                synonyms.append(i.name())

    # Combine the synonyms into the bag of words
    bag_of_words.extend(set(synonyms))

    # Loop until desired number of backronyms have been generated
    i = 0
    while i < n_results:
        # MAIGC
        backronym = backronym_loop(acronym, bag_of_words)

        print("Backronym: %s" % backronym)
        i += 1
