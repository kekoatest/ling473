# written by unclenacho
# read a SGML file
# remove markup
# remove special chars, except A-Za-z\'
# remove ' from begining and end of word
# make all lowercase
# count occurences of each word
# print words in descending order by count, with count
import re # regexlibrary
import operator # library that allwos me to access doctinoary values
import os # library that allows me to loop the files in a folder

wordswithcount = {} # dictionary of word, count
readytoprint = [] # list of count, word - will be sorted

# loop through all files in DB
folder = "/corpora/LDC/LDC02T31/nyt/2000"
for file in os.listdir(folder):

    filepath = os.path.join(folder, file)

# read text from file
    openfile = open(filepath, 'r')
    text = openfile.read()
    openfile.close()

# remove markup
    newtext = re.sub("<[^>]*>", " ", text)
# remove special chars
    newtext = re.sub("[^A-Za-z']", " ", newtext)
# remove ' at begining of word - including multiple
    newtext = re.sub(" \'*", " ", newtext)
# remove ' at end of word - including multiple
    newtext = re.sub("\'* ", " ", newtext)

# make lower case
    newtext = newtext.lower()
    wordlist = newtext.split(" ") # list of all words in current file

# loop through all words in current file
# add new words to dictionary, add one to count for each word instance
    for word in wordlist:
# exclude empty string
        if word == "":
            word = word
        elif word in wordswithcount:
            wordswithcount[word] += 1
        else:
            wordswithcount[word] = 1

# created list of dictionary items, reverse sorted by tally
readytoprint = sorted(wordswithcount.items(), key=operator.itemgetter(1), reverse=True)

for word in readytoprint:
    print(word[0] + "\t" + str(word[1]))
