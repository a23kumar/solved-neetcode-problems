class TrieNode:
    def __init__(self):
        self.children = dict()
        self.endOfWord = False

class WordDictionary:

    def __init__(self):
        self.trienode = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.trienode
        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.endOfWord = True

    def search(self, word: str) -> bool:
        
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                
                if c == '.':
                    for child_node in cur.children.values():
                        if dfs(i + 1, child_node):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
                    
            return cur.endOfWord
        
        return dfs(0, self.trienode)