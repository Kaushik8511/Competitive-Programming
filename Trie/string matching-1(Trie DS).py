#return if s is substring of t or not

s = "wehngsdndsuhrouabfden"
t = "fefuafidajigffjakiogteiajndangfoitjwehngsdndsuhrouabfdenjfauhfuweyhujafsdnfabfded"



class TrieNode:
    def __init__(self):
        self.end = False
        self.child = [None for i in range(26)]

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self,s):
        ptr = self.root
        for c in s:
            ind = ord(c)-ord('a')
            if ptr.child[ind]==None:
                ptr.child[ind]=TrieNode()
            ptr=ptr.child[ind]
        ptr.end=True

    def search(self,s):
        ptr = self.root
        for c in s:
            ind = ord(c)-ord('a')
            if ptr.child[ind]==None:return False
            ptr = ptr.child[ind]
        return ptr.end

def match(s,t):
    m,n = len(t),len(s)
    if n>m:return False
    trie = Trie()
    for i in range(m-n+1):
        trie.insert(t[i:i+n])
    return trie.search(s)

print(match(s,t))
        
        
    
