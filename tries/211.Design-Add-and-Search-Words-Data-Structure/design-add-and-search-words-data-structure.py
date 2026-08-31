class DictionaryNode:
    def __init__(self):
        self.children = {}
        self.isLastLetter = False

class WordDictionary:

    def __init__(self):
        self.root = DictionaryNode()

    def addWord(self, word: str) -> None:
        temp = self.root # of type DictionaryNode
        for letter in word:
            if letter not in temp.children:
                temp.children[letter] = DictionaryNode()
            temp = temp.children[letter]
        temp.isLastLetter = True

    def search(self, word: str) -> bool:
        def dfs(node, index):
            temp = node # DictionaryNode type
            if index == len(word):
                return node.isLastLetter
                
            if word[index] in node.children:
                temp = node.children[word[index]]
                return dfs(temp, index + 1)

            if word[index] == ".":
                output = False
                for child in temp.children.values():
                    if dfs(child, index + 1):
                        return True
            
            return False

        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
