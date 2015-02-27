'''
MODIFIEDSUFFIXTRIECONSTRUCTION(Text)
        Trie <- a graph consisting of a single node root
        for i <- 0 to |Text| - 1
            currentNode <- root
            for j <- i to |Text| - 1
                currentSymbol <- j-th symbol of Text
                if there is an outgoing edge from currentNode labeled by currentSymbol
                    currentNode <- ending node of this edge
                else
                    add a new node newNode to Trie
                    add an edge newEdge connecting currentNode to newNode in Trie
                    Symbol(newEdge) <- currentSymbol
                    Position(newEdge) <- j
                    currentNode <- newNode
            if currentNode is a leaf in Trie
                assign label i to this leaf
        return Trie

MODIFIEDSUFFIXTREECONSTRUCTION(Text)
        Trie <- MODIFIEDSUFFIXTRIECONSTRUCTION
        for each non-branching path Path in Trie
            substitute Path by a single edge edge connecting the first and last nodes of Path
            Position(edge) <- Position(first edge of Path)
            Length(edge) <- number of edges of Path
        return Trie
        
    MaximalNonBranchingPaths(Graph)
        Paths <- empty list
        for each node v in Graph
            if v is not a 1-in-1-out node
                if out(v) > 0
                    for each outgoing edge (v, w) from v
                        NonBranchingPath <- the path consisting of the single edge (v, w)
                        while w is a 1-in-1-out node
                            extend NonBranchingPath by the outgoing edge (w, u) from w 
                            w <- u
                        add NonBranchingPath to the set Paths
        for each isolated cycle Cycle in Graph
            add Cycle to Paths
        return Paths
'''    
def ModSuffixTrie(Text):
    trie={}
    trie[0]={}
    newNode=0
    for i in range(0,len(Text)):
        #print 'cycle',i
        currentNode=0
        for j in range(i,(len(Text))):
            currentSymbol=Text[j]
            #print 'currentSymbol',currentSymbol
            if currentSymbol in trie[currentNode].keys():
                currentNode=trie[currentNode][currentSymbol][0]
                #print 'currentNode',currentNode
            else:
                newNode+=1
                trie[newNode]={}
                trie[currentNode][currentSymbol]=[newNode,j]
                currentNode=newNode
                #print trie
        if trie[currentNode]=={}:
            trie[currentNode]=i
    return trie

def NonBranchingPaths(graph):  
    paths=[]
    for v in graph.keys():
        #print '----\nv',v
        if(isinstance(graph[v],int)):
            continue
        if len(graph[v].keys())!=1:
            #print 'not 1-1' #branching
            if len(graph[v].keys())>0:
                vkeys=graph[v].keys()
                for vkey in vkeys:
                    w=graph[v][vkey][0]
                    #print '-->',vkey,w,graph[w]
                    nbp=vkey
                    if(not(isinstance(graph[w],int))):
                        while len(graph[w].keys())==1:
                            sym=graph[w].keys()[0]
                            #print 'in',sym
                            nbp+=sym
                            w=graph[w].values()[0][0]
                            if(isinstance(graph[w],int)):
                                break
                    if nbp!='':paths.append(nbp)
                    #print 'paths:',paths
    return paths
trie=ModSuffixTrie('ATATCGTTTTATCGTT$')
print trie
paths=NonBranchingPaths(trie)
print paths
maxrepeat=''
for p in set(paths):
    print p,paths.count(p)
    if paths.count(p)==1:continue
    if len(p)>len(maxrepeat):
        maxrepeat=p
print set(paths)
print maxrepeat

# file1='C:/Users/dlow/Documents/Dropbox/Coursera/Bioinformatics Algorithms 2/1/answer_296_4.txt'
# f1=open(file1,'w')
# for p in paths:
#     f1.write('{0}\n'.format(p))
# f1.close()