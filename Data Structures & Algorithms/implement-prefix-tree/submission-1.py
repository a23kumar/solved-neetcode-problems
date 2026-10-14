class TrieNode:
    def __init__(self):
        self.children = dict()
        self.isEndOfWord = False

class PrefixTree:
    def __init__(self):
        self.trienode = TrieNode()
        
    def insert(self, word: str) -> None:
        cur = self.trienode
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        # for each char, we want to determine if that leter is in the children
        # if not, immediately return false
        # if we make it all the way to the end and cur.isEndOfWord is true, return true
        cur = self.trienode
        for c in word:
            if c not in cur.children:
                return False

            cur = cur.children[c]
        
        return cur.isEndOfWord
        

    def startsWith(self, prefix: str) -> bool:
        cur = self.trienode
        for c in prefix:
            if c not in cur.children:
                return False
            cur = cur.children[c]
        
        return True

        
        