import os

class Node:
    def __init__(self, label=None, data=None):
        self.label = label
        self.data = data
        self.children = dict()

    def addChild(self, key, data=None):
        if not isinstance(key, Node):
            self.children[key] = Node(key, data)
        else:
            self.children[key.label] = key

    def __getitem__(self, key):
        return self.children[key]

class Trie:
    def __init__(self):
        self.head = Node()

    def __getitem__(self, key):
        return self.head.children[key]

    def add(self, word):
        current_node = self.head
        word_finished = True

        for i in range(len(word)):
            if word[i] in current_node.children:
                current_node = current_node.children[word[i]]
            else:
                word_finished = False
                break

        # For ever new letter, create a new child node
        if not word_finished:
            while i < len(word):
                current_node.addChild(word[i])
                current_node = current_node.children[word[i]]
                i += 1

        # Let's store the full word at the end node so we don't need to
        # travel back up the tree to reconstruct the word
        current_node.data = word

    def has_word(self, word):
        if word == '':
            return False
        if word == None:
            raise ValueError('Trie.has_word requires a not-Null string')

        # Start at the top
        current_node = self.head
        exists = True
        for letter in word:
            if letter in current_node.children:
                current_node = current_node.children[letter]
            else:
                exists = False
                break

        # Still need to check if we just reached a word like 't'
        # that isn't actually a full word in our dictionary
        if exists:
            if current_node.data == None:
                exists = False

        return exists

    def start_with_prefix(self, prefix):
        """ Returns a list of all words in tree that start with prefix """
        words = list()
        if prefix == None:
            raise ValueError('Requires not-Null prefix')

        # Determine end-of-prefix node
        top_node = self.head
        for letter in prefix:
            if letter in top_node.children:
                top_node = top_node.children[letter]
            else:
                # Prefix not in tree, go no further
                return words

        # Get words under prefix
        if top_node == self.head:
            queue = [node for key, node in top_node.children.iteritems()]
        else:
            queue = [top_node]

        # Perform a breadth first search under the prefix
        # A cool effect of using BFS as opposed to DFS is that BFS will return
        # a list of words ordered by increasing length
        while queue:
            current_node = queue.pop()
            if current_node.data != None:
                # Isn't it nice to not have to go back up the tree?
                words.append(current_node.data)

            queue = [node for key,node in current_node.children.items()] + queue

        return words

    def getData(self, word):
        """ This returns the 'data' of the node identified by the given word """
        if not self.has_word(word):
            raise ValueError('{} not found in trie'.format(word))

        # Race to the bottom, get data
        current_node = self.head
        for letter in word:
            current_node = current_node[letter]

        return current_node.data


resource = open("/opt/dropbox/17-18/473/project4/targets")
targets = resource.readlines()

trie = Trie()
for line in targets:
    trie.add(line[:-1])
#print(trie.has_word('GTTTTTACATTATCTTGTTATCTTTCAACCTTGGTTGAATTAGGCAAGGTAGGTATCATTGTAGAGCTCACTAGGGAGTCTTTTTTGGTTCAACTAAACAGTAAGGTTCATAAGACTGTCATGGGCCAT'))
#print(sorted(trie.start_with_prefix('G')))

writetofile = open("output.txt", "w+")

folder = "/opt/dropbox/17-18/473/project4/hg19-GRCh37/"
for file in os.listdir(folder):

    filepath = os.path.join(folder, file)

    print(filepath)
    writetofile.write(filepath + "\n")

    if filepath == "/opt/dropbox/17-18/473/project4/hg19-GRCh37/chr1.dna":
# read text from file
        openfile = open(filepath, 'r')
        text = openfile.read()
        text = text.upper()
        openfile.close()

        i = 0
        while i <= len(text):
            j = i + 1

            if i % 1000000 == 0:
                print("i at position " + str(i))
            elif i == 0:
                print("Starting")

            while j <= len(text):
                if trie.has_word(text[i:j]) ==  True:
                    print("\tHexvalue\t" + text[i:j])
                    writetofile.write("\tHexvalue\t" + text[i:j] + "\n")

                if j % 1000000 == 0:
                    print("j at position " + str(j))

                if j - i < 189:
                    j = len(text)

                j += 1

            i += 1
