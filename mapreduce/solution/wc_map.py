import sys

# Output should be: <key '\t' value>
for line in sys.stdin:
    line = line.lower().rsplit()
    for word in line:
        # Every instance of <word> will be sent to the same reducer for processing
        print('{}\t{}'.format(word, 1))
