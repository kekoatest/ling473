import pprint
from collections import deque

pp = pprint.PrettyPrinter(indent=4)

inp = input("Enter a sentence to show as trie\n")
words = inp.split(" ")
trie = {}


def trie_recursion(trie_ds, word):
    try:
        letter = word.popleft()
        out = trie_recursion(trie_ds.get(letter, {}), word)
    except IndexError:
        # End of the word
        return {}

    # Dont update if letter already present
    if letter not in trie_ds:
        trie_ds[letter] = out

    return trie_ds

for word in words:
    # Go through each word
    trie = trie_recursion(trie, deque(word))

pprint.pprint(trie)
