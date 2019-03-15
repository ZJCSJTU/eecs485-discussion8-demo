import sys

# Output should be: <key '\t' value>
for line in sys.stdin:
    # Preprocess the input
    line = line.lower().rsplit()
    for word in line:
        # TODO: WRITE YOUR CODE HERE
        print(word, "\t1")
