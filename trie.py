from collections import defaultdict


class TrieNode:
    def __init__(self, char=''):
        self.children = defaultdict(TrieNode)
        self.char = char

    def __str__(self):
        msg = "node: " + self.char
        msg += "/n chilren: "
        msg += ", ".join([key for key in self.children.keys()])
        return msg


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.node = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        :type word: object
        """
        current = self.node
        for c in word:
            if c not in current.children:
                current.children[c] = TrieNode(c)
            current = current.children[c]
        if '' not in current.children:
            current.children[''] = TrieNode('')

    def search(self, word: str) -> bool:

        current = self.node
        for c in word:
            if c not in current.children:
                return False
            current = current.children[c]
        if '' not in current.children:
            return False
        return True

    def startsWith(self, prefix: str) -> bool:
        current = self.node
        for c in prefix:
            if c not in current.children:
                return False
            current = current.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# word = "what"
# word2 = "whose"
# word3 = "who"
# word4 = "why"
# prefix = 'wha'
# obj = Trie()
#
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)


obj = Trie()


def do_nothing(var):
    pass


name_dispatcher = {"Trie": do_nothing, 'search': obj.search, 'insert': obj.insert, 'startsWith': obj.startsWith}
funcs = ["Trie", "insert", "search", "search", "startsWith", "insert", "search"]

input = [[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]

for i in range(len(funcs)):
    func = name_dispatcher[funcs[i]]
    var = input[i][0] if len(input[i]) > 0 else 1;
    result = func(var)
    print(result, sep=', ')
