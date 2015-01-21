from sys import argv

script, filename = argv

my_file = open(filename)



d = {}
for line in my_file:            # go through each line in my_file
    line = line.strip()         # strip each line in the file and bind to line
    entries = line.split()      # split each line by spaces and bind to entries. Result is a list of all the words in each line.
    for word in entries:        # for each word in the entries list          
        if word in d:           # if the word is in the dictionary 
            d[word] = d[word] + 1     # add one to the current count of the word
        else:                      
             d[word] = 1            # add the word to the dictionary and add 1 to the value. now we have a dictionary that counts all words

for item in d.iteritems():             # for each item in the list of tuples
    print "%s %d" % (item[0], item[1])  # print the first item and the second item


