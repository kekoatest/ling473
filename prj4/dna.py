import os

# -----------------------------------------------------------------------------
# Node class with label, array for children, and bool to mark the node as
# final, meaning a word that was entered into the trie ends on this Node
# final helps identify both 'cat' and 'cats'
class Node(object):
    def __init__(self, data, endchar):
        self.data = data
        self.children = [None] * 4
        self.final = endchar

# adds children based on location in array. Array of len 4 for A C G T
    def add_child(self, obj):
        if obj.data == "A":
            self.children[0] = obj
        elif obj.data == "C":
            self.children[1] = obj
        elif obj.data == "G":
            self.children[2] = obj
        elif obj.data == "T":
            self.children[3] = obj
        else:
            raise ValueError('Children can only be A, C, G, or T')

# -----------------------------------------------------------------------------
# Trie class
#
class Trie:
    def __init__(self):
        self.head = Node("head", False)

    def access(self):
        return self.head

    def add(self, word):
        current_node = self.head
        word_finished = True

        x = 0

        for i in range(len(word)):
            if word[i] == "A":
                if current_node.children[0] != None:
                    current_node = current_node.children[0]
                    x += 1
                    if x == len(word):
                        current_node.final = True
                else:
                    word_finished = False
            elif word[i] == "C":
                if current_node.children[1] != None:
                    current_node = current_node.children[1]
                    x += 1
                    if x == len(word):
                        current_node.final = True
                else:
                    word_finished = False
            elif word[i] == "G":
                if current_node.children[2] != None:
                    current_node = current_node.children[2]
                    x += 1
                    if x == len(word):
                        current_node.final = True
                else:
                    word_finished = False
            elif word[i] == "T":
                if current_node.children[3] != None:
                    current_node = current_node.children[3]
                    x += 1
                    if x == len(word):
                        current_node.final = True
                else:
                    word_finished = False
            if not word_finished:
                break

        # For ever new letter, create a new child node
        if not word_finished:
            while x < len(word):
                if x == len(word)-1:
                    current_node.add_child(Node(word[x], True))
                else:
                    if word[x] == "A":
                        current_node.add_child(Node(word[x], False))
                        current_node = current_node.children[0]
                    elif word[x] == "C":
                        current_node.add_child(Node(word[x], False))
                        current_node = current_node.children[1]
                    elif word[x] == "G":
                        current_node.add_child(Node(word[x], False))
                        current_node = current_node.children[2]
                    elif word[x] == "T":
                        current_node.add_child(Node(word[x], False))
                        current_node = current_node.children[3]
                x += 1

    def has_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')

        current_node = self.head
        exists = True
        for letter in word:
            if letter == "A":
                if current_node.children[0] != None:
                    current_node = current_node.children[0]
                else:
                    exists = False
            elif letter == "C":
                if current_node.children[1] != None:
                    current_node = current_node.children[1]
                else:
                    exists = False
            elif letter == "G":
                if current_node.children[2] != None:
                    current_node = current_node.children[2]
                else:
                    exists = False
            elif letter == "T":
                if current_node.children[3] != None:
                    current_node = current_node.children[3]
                else:
                    exists = False

        if exists:
            if current_node.data == None:
                exists = False

        return exists


# -----------------------------------------------------------------------------
# Function that searches DNA files for strings in trie
def search(head):
    extracredit = ""
    current = head
    folder = "/opt/dropbox/17-18/473/project4/hg19-GRCh37/"
    for file in os.listdir(folder):

        filepath = os.path.join(folder, file)

        print(filepath)

        extracredit += filepath + "\n"

# read text from file
        openfile = open(filepath, 'r')
        text = openfile.read()
        text = text.upper()
        openfile.close()

        i = 0
        while i < len(text):
            j = i
            current = head

            while j < len(text):

                if text[j] == "A":
                    if current.final == True:
                        print("\t" + str(format(i, '08X')) + "\t" + text[i:j])
                        extracredit += "\t" + str(format(i, '08X')) + "\t" + text[i:j]
                    if current.children[0] != None:
                        current = current.children[0]
                    else:
                        break
                elif text[j] == "C":
                    if current.final == True:
                        print("\t" + str(format(i, '08X')) + "\t" + text[i:j])
                        extracredit += "\t" + str(format(i, '08X')) + "\t" + text[i:j]
                    if current.children[1] != None:
                        current = current.children[1]
                    else:
                        break
                elif text[j] == "G":
                    if current.final == True:
                        print("\t" + str(format(i, '08X')) + "\t" + text[i:j])
                        extracredit += "\t" + str(format(i, '08X')) + "\t" + text[i:j]
                    if current.children[2] != None:
                        current = current.children[2]
                    else:
                        break
                elif text[j] == "T":
                    if current.final == True:
                        print("\t" + str(format(i, '08X')) + "\t" + text[i:j])
                        extracredit += "\t" + str(format(i, '08X')) + "\t" + text[i:j]
                    if current.children[3] != None:
                        current = current.children[3]
                    else:
                        break
                else:
                    break

                j += 1

            i += 1
    return extracredit


def fill(words):
    resource = open("/opt/dropbox/17-18/473/project4/targets")
    targets = resource.readlines()
    for line in targets:
        words.add(line[:-1])


# Extracredit function -  Print data by sequence rather than file
# This function is very poorly coded in terms of repetition and time and space complexity
# However, the function takes only a second to run.
# Therefore, the ugly script and implementation are marked as WONTFIX
def ec(extracredit):
    text = extracredit.split("\n")

    empty = {}
    chr1 = {}
    chr2 = {}
    chr3 = {}
    chr4 = {}
    chr5 = {}
    chr6 = {}
    chr7 = {}
    chr8 = {}
    chr9 = {}
    chr10 = {}
    chr11 = {}
    chr12 = {}
    chr13 = {}
    chr14 = {}
    chr15 = {}
    chr16 = {}
    chr17 = {}
    chr18 = {}
    chr19 = {}
    chr20 = {}
    chr21 = {}
    chr22 = {}
    chrX = {}
    chrY = {}

    genome = []

    genome.append(None)
    genome.append(chr1)
    genome.append(chr2)
    genome.append(chr3)
    genome.append(chr4)
    genome.append(chr5)
    genome.append(chr6)
    genome.append(chr7)
    genome.append(chr8)
    genome.append(chr9)
    genome.append(chr10)
    genome.append(chr11)
    genome.append(chr12)
    genome.append(chr13)
    genome.append(chr14)
    genome.append(chr15)
    genome.append(chr16)
    genome.append(chr17)
    genome.append(chr18)
    genome.append(chr19)
    genome.append(chr20)
    genome.append(chr21)
    genome.append(chr22)
    genome.append(chrX)
    genome.append(chrY)

    counter = -1

    for line in text:
        if line == "":
            crazy = "this is stupid"
        elif '/' in line:
            text = line.split('/')
            if text[len(text)-1] == "chr1.dna":
                counter = 1
            elif text[len(text)-1] == "chr2.dna":
                counter = 2
            elif text[len(text)-1] == "chr3.dna":
                counter = 3
            elif text[len(text)-1] == "chr4.dna":
                counter = 4
            elif text[len(text)-1] == "chr5.dna":
                counter = 5
            elif text[len(text)-1] == "chr6.dna":
                counter = 6
            elif text[len(text)-1] == "chr7.dna":
                counter = 7
            elif text[len(text)-1] == "chr8.dna":
                counter = 8
            elif text[len(text)-1] == "chr9.dna":
                counter = 9
            elif text[len(text)-1] == "chr10.dna":
                counter = 10
            elif text[len(text)-1] == "chr11.dna":
                counter = 11
            elif text[len(text)-1] == "chr12.dna":
                counter = 12
            elif text[len(text)-1] == "chr13.dna":
                counter = 13
            elif text[len(text)-1] == "chr14.dna":
                counter = 14
            elif text[len(text)-1] == "chr15.dna":
                counter = 15
            elif text[len(text)-1] == "chr16.dna":
                counter = 16
            elif text[len(text)-1] == "chr17.dna":
                counter = 17
            elif text[len(text)-1] == "chr18.dna":
                counter = 18
            elif text[len(text)-1] == "chr19.dna":
                counter = 19
            elif text[len(text)-1] == "chr20.dna":
                counter = 20
            elif text[len(text)-1] == "chr21.dna":
                counter = 21
            elif text[len(text)-1] == "chr22.dna":
                counter = 22
            elif text[len(text)-1] == "chrX.dna":
                counter = 23
            elif text[len(text)-1] == "chrY.dna":
                counter = 24
        else:
            datas = line.split("\t")
            genome[counter][datas[2]] = datas[1]

    printme = {}
    number = 1
    while number < 25:
        name = "XXX"
        if number == 1:
            name = "chr1.dna"
        elif number == 2:
            name = "chr2.dna"
        elif number == 3:
            name = "chr3.dna"
        elif number == 4:
            name = "chr4.dna"
        elif number == 5:
            name = "chr5.dna"
        elif number == 6:
            name = "chr6.dna"
        elif number == 7:
            name = "chr7.dna"
        elif number == 8:
            name = "chr8.dna"
        elif number == 9:
            name = "chr9.dna"
        elif number == 10:
            name = "chr10.dna"
        elif number == 11:
            name = "chr11.dna"
        elif number == 12:
            name = "chr12.dna"
        elif number == 13:
            name = "chr13.dna"
        elif number == 14:
            name = "chr14.dna"
        elif number == 15:
            name = "chr15.dna"
        elif number == 16:
            name = "chr16.dna"
        elif number == 17:
            name = "chr17.dna"
        elif number == 18:
            name = "chr18.dna"
        elif number == 19:
            name = "chr19.dna"
        elif number == 20:
            name = "chr20.dna"
        elif number == 21:
            name = "chr21.dna"
        elif number == 22:
            name = "chr22.dna"
        elif number == 23:
            name = "chr23.dna"
        elif number == 24:
            name = "chr24.dna"

        for k in genome[number]:
            v = genome[number][k]
            if k not in printme:
                printme[k] = "\n\t" + v + "\t" + name
            elif k in printme:
                printme[k] += "\n\t" + v + "\t" + name
        number += 1

    writefile = open("extra-credit", "w+")

    for k in printme:
        v = printme[k]
        writefile.write(k + v + "\n")


# -----------------------------------------------------------------------------
# MAIN Function

# Initialize Trie
words = Trie()

# Fill Tree from targets
fill(words)

# get the head node of the tree
head = words.access()

# Search function
extracredit = search(head)

# extracredit function
ec(extracredit)
