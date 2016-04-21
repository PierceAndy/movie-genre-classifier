#!/usr/bin/python
from __future__ import division
import sys
import getopt
import string
import operator
from nltk.corpus import stopwords
from nltk.stem import porter
from nltk.util import ngrams

"""
Evaluates genre of given synopsis using a character based n-gram.
Reasons for choosing character based n-grams covered in email.
This program should fulfil the requirements of the challenge, and return the genres and their respective probability
percentages in the same line as the synopsis in the output file.
"""


n = 2 # size of n-gram, the larger the value, the larger the training data has to be
smoothing = 1 # smoothing value, to avoid problems with division by 0
imdb_genres = [ # Retrieved from http://www.imdb.com/interfaces
    "Short",
    "Drama",
    "Comedy",
    "Documentary",
    "Action",
    "Thriller",
    "Romance",
    "Animation",
    "Family",
    "Horror",
    "Music",
    "Crime",
    "Adventure",
    "Fantasy",
    "Sci-Fi",
    "Mystery",
    "Biography",
    "History",
    "Sport",
    "Musical",
    "War",
    "Western",
    "Reality-TV",
    "News",
    "Talk-Show",
    "Game-Show",
    "Film-Noir"
]


def main():
    input_file_b = input_file_t = output_file = None
    try:
        opts, args = getopt.getopt(sys.argv[1:], 'b:t:o:')
    except getopt.GetoptError, err:
        usage()
        sys.exit(2)
    for o, a in opts:
        if o == '-b':
            input_file_b = a
        elif o == '-t':
            input_file_t = a
        elif o == '-o':
            output_file = a
        else:
            assert False, "unhandled option"
    if input_file_b is None or input_file_t is None or output_file is None:
        usage()
        sys.exit(2)

    LM, total_count = build_LM(input_file_b)
    test_LM(input_file_t, output_file, LM, total_count)


def usage():
    """Explains usage rules to user
    """
    print "usage: " + sys.argv[0] + " -b input-file-for-building-LM -t input-file-for-testing-LM -o output-file"


def build_LM(in_file):
    """Build language models using each line in training data
    Each line in in_file contains genre labels and the synopsis separated by a whitespace
    LM will be built with word n-grams for accuracy, and unigrams for testing speed
    LM is a dictionary (with n-gram keys) of dictionaries (with genre keys) with count values
    """
    print "Building LM..."

    LM = dict()
    total_count = {genre: smoothing for genre in imdb_genres}
    
    with open(in_file) as training_data:
        for line in training_data:

            genres, synopsis = line.split(" ", 1)
            genres = genres.split("/") # get list of genres related to synopsis
            synopsis_ngrams = normalize_text(synopsis)

            # Go through all possible n-grams from text
            for ngram in synopsis_ngrams:

                if ngram not in LM:
                    # if n-gram is a new entry
                    LM[ngram] = create_entry()

                for genre in genres:
                    try:
                        LM[ngram][genre] += 1
                        total_count[genre] += 1
                    except Exception as error:
                        # At times, synopsis received from IMDB is incomplete or poorly formatted
                        #print synopsis + str(error)
                        error

    return LM, total_count
        

def test_LM(in_file, out_file, LM, total_count):
    """Test the language models on a file containing lines of synopsis
    Each line of in_file contains a synopsis for a movie
    Prints out the percentage chance probability of the given synopsis belonging to each genre type
    """
    print "Testing LM..."

    with open(in_file) as test_data, open(out_file, 'w+') as predict_data:
        for synopsis in test_data:

            num_matches = 0
            ngram_genre_count = {genre: 0 for genre in imdb_genres}
            total_ngrams = 0

            synopsis_ngrams = normalize_text(synopsis)

            # go through all possible n-grams from text
            for ngram in synopsis_ngrams:

                prob = {genre: 0 for genre in imdb_genres} # probabilities that this ngram belongs to each genre

                if ngram in LM: # ignoring n-grams not found in LM
                    total_ngrams += 1
                    for genre in imdb_genres:
                        # Get normalized probability that this n-gram belongs to each genre
                        prob[genre] = LM[ngram][genre] / total_count[genre]

                    num_matches += 1
                    genre_with_max_prob = max(prob.iteritems(), key=operator.itemgetter(1))[0]

                    # Keep track of the n-gram genre counts
                    # Only increment the count for the genre that this n-gram most likely belongs to
                    ngram_genre_count[genre_with_max_prob] += 1

            # if text has no matches in LM at all, probably belongs to an unknown genre
            if (num_matches / total_ngrams) < 0.3: # set to 0.3 because of the small size of the training data
                predict_data.write("Insufficient data to make judgment")
            else:
                # Write probabilities of each genre to output file
                result = ""
                ngram_genre_prob = dict()

                # Calculate likelihood of given synopsis belonging to a genre based on how many n-grams are likely to belong to that genre
                for genre in imdb_genres:
                    ngram_genre_prob[genre] = 100 * ngram_genre_count[genre]/total_ngrams

                # Sort genre probabilities from highest value to lowest, as list of tuples to preserve order
                ngram_genre_prob = sorted(ngram_genre_prob.items(), key=operator.itemgetter(1), reverse=True)

                for genre_prob in ngram_genre_prob:
                    result += str(genre_prob[0]) + ": " + str(genre_prob[1]) + "%, "
                predict_data.write(result + "\n")


def create_entry():
    """Creates a new entry for each new n-gram in the LM's dictionary
    to keep track of the count of that n-gram for each genre.
    """
    return {genre: 0 for genre in imdb_genres}


def normalize_text(text):
    """Normalizes text, and returns normalized text in n-gram format"""

    stemmer = porter.PorterStemmer()

    text = text.translate(None, string.punctuation) # remove punctuation
    text = text.lower() # lowercase
    text = text.split() # tokenize
    text = [word for word in text if word not in set(stopwords.words("english"))] # remove stopwords)

    try: # Stemmer is unable to process certain unicode character from IMDB's information
        text = [stemmer.stem(word) for word in text] # stem with porter stemmer
    except Exception as error:
        #print text
        #print "\n" + str(error)
        error
    text_ngrams = ngrams(text, n) # create n-grams

    return text_ngrams


if __name__ == "__main__":
    main()
