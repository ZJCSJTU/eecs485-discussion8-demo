import collections
import sys

words = collections.defaultdict(int)
# Append all the words in the input files to dictionary of word-count pairs
for line in sys.stdin:
    split_line = line.rsplit()
    word = split_line[0]
    count = int(split_line[1])
    words[word] += 1

# Output should be: <word '\t' word_count>
for key, val in words.items():
    print('{}\t{}'.format(key, val))
