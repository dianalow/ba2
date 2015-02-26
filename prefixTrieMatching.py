'''
#2 prefix Trie
'''
from trie_construction import Trie
file1='C:/Users/dlow/Documents/Dropbox/Coursera/Bioinformatics Algorithms 2/1/dataset_294_8.txt'

f1=open(file1,'r')

patterns=[]
for n,i in enumerate(f1):
    if n==0: 
        text0=i.strip('\n\r')
        continue
    i0=i.strip('\n\r')
    patterns.append(i0)

f1.close()

trie=Trie(patterns)
def prefixTrieMatching(text,trie):
    text+='-'
    fulltext=''
    textloc=0
    symbol=text[textloc]
    v=0
    while True:
        if trie[v]=={}:
            return 1
        elif symbol in trie[v].keys():
            fulltext+=symbol
            textloc+=1
            w=trie[v][symbol]
            symbol=text[textloc]
            v=w
        else:
            #print('No matches found.')
            return 0

def TrieMatching(text,trie):
    startpos=0
    while text!='':
        result=prefixTrieMatching(text,trie)
        if result==1:
            print startpos,
        startpos+=1
        text=text[1:]
        
TrieMatching(text0,trie)


