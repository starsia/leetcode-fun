class TrieNode:
    def __init__(self):
        self.children = {}
        self.isLastLetter = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        current = self.root # a TrieNode
        for letter in word:
            if letter not in current.children:
                current.children[letter] = TrieNode()
            current = current.children[letter]
        current.isLastLetter = True
        

    def search(self, word: str) -> bool:
        current = self.root
        for letter in word:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        if current.isLastLetter == True:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        for letter in prefix:
            if letter in current.children:
                current = current.children[letter]
            else:
                return False
        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
