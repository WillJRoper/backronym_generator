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
import numpy as np
import itertools


def backronym_loop(acronym, words, ini_synsets):

    # Set up lists to hold each letters words
    words_for_letters = []
    while len(words_for_letters) < len(acronym):
        words_for_letters.append([])

    # Loop over letters in the desired acronym
    for ind, l in enumerate(acronym):

        # Loop over words in the bag of words and include them if the letter
        # is in them
        for w in words:
            if l in w.lower():
                words_for_letters[ind].append(w)

    # Create a list to store the list of backacronyms
    backronyms = list(itertools.product(*words_for_letters))

    # Remove duplicates
    backronyms = sorted(backronyms)
    backronyms = list(k for k, _ in itertools.groupby(backronyms))

    return backronyms


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
    n_results = 10
    acronym = sys.argv[1].lower()
    ini_bag_of_words = sys.argv[2:]
    bag_of_words = []
    bag_of_words.extend(ini_bag_of_words)

    # Include some stop words that could be useful
    bag_of_words.extend(["the", "and", "is", "of", "in", "for",
                         "from", "or", "a", "an", "by"])

    # Create a list of synsets for the initial bag of words for
    # similarity computing
    ini_synsets = []
    for word in ini_bag_of_words:
        ini_synsets.extend(wordnet.synsets(word))

    # Set up list for the synonyms
    synonyms = []

    # Expand the bag of words with synonyms
    for word in bag_of_words:  # loop over the bag of words

        # Loop over synonyms for this word
        for syn in wordnet.synsets(word):

            # Store maximum similarity to initial words
            max_sim = 0
            for ini_syn in ini_synsets:
                d = wordnet.wup_similarity(ini_syn, syn)

                if d > max_sim:
                    max_sim = d

            # Only assign these synonyms if sufficiently similar
            if max_sim > 0.75:

                for i in syn.lemmas():

                    # Ensure this word contains letters in the acronym
                    for l in acronym:
                        if l in i.name():
                            synonyms.append(i.name())
                            break

    # Combine the synonyms into the bag of words
    bag_of_words.extend(set(synonyms))

    # MAIGC
    backronyms = backronym_loop(acronym, bag_of_words, ini_synsets)

    # Loop over backronyms print out n top results
    i = 0
    while i < n_results:

        print("Backronym:", backronyms[i])
        i += 1
