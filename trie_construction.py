'''
#1 Trie construction problem
'''
file1='C:/Users/dlow/Documents/Dropbox/Coursera/Bioinformatics Algorithms 2/1/trie.txt'

f1=open(file1,'r')

patterns=[]
for n,i in enumerate(f1):
    i0=i.strip('\n\r')
    patterns.append(i0)

f1.close()

def Trie(patterns):  
    trie={}
    root=0
    newNode=1
    for text in patterns:
        currentNode=root
        for m,j in enumerate(text):
            if currentNode not in trie.keys(): trie[currentNode]={}
            if j in trie[currentNode].keys():
                currentNode=trie[currentNode][j]
            else:
                trie[newNode]={}
                trie[currentNode][j]=newNode
                currentNode=newNode
                newNode+=1           
    return trie

trie=Trie(patterns)
print trie
for node in trie.keys():
    nextnode=trie[node].keys()
    for n in nextnode:
        print '{0}->{1}:{2}'.format(node,trie[node][n],n)      