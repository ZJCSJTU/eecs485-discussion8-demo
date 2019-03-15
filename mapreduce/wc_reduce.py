import collections
import sys

words = collections.defaultdict(int)
# Append all the words in the input files to dictionary of word-count pairs
for line in sys.stdin:
    split_line = line.rsplit()
    # TODO: IMPLEMENT ME

# Output should be: <word '\t' word_count>
for key, val in words.items():
    # TODO: PRINT KEY-VALUE PAIRS
