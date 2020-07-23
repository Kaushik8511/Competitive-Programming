class TrieNode:
    def __init__(self):
        self.count=1
        self.end=0
        self.child = [None for i in range(26)]

class Trie:
    def __init__(self):
        self.root=TrieNode()

    def insert(self,s):
        ptr = self.root
        for char in s:
            ind=ord(char)-ord('a')
            if not ptr.child[ind]:
                ptr.child[ind]=TrieNode()
                ptr = ptr.child[ind]
            else:
                ptr=ptr.child[ind]
                ptr.count+=1
        ptr.end+=1

    def search(self,s):
        ptr=self.root
        for char in s:
            ind = ord(char)-ord('a')
            if ptr.child[ind]==None:return False
            ptr=ptr.child[ind]
        if ptr.end>0:return "search "+s+" : "+str(ptr.end)
        return False

    def startWith(self,s):
        ptr=self.root
        for char in s:
            ind=ord(char)-ord('a')
            if ptr.child[ind]==None:return 0
            ptr=ptr.child[ind]
        return "start with "+s+" : "+str(ptr.count)

self=Trie()
print(self.insert('apple'))
print(self.insert('add'))
print(self.startWith('ap'))
print(self.insert('beer'))
print(self.search('add'))
print(self.search('app'))
print(self.search('apple'))
print(self.insert('apple'))
print(self.search('apple'))
print(self.startWith('a'))

        
                
            
            
        
