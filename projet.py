import copy
def nodesOfDegreeLessOrEqual(graph,degree):
    List=[]
    
    for k,v in graph.items():
        if degree>=len(v):
            List.append(k)
    
    return List

def deleteNodes(graph,nodes):
    for node in nodes:
        
        for neighbor in graph[node]:
            if neighbor != node:
                while node in graph[neighbor]:
                    graph[neighbor].remove(node)
            
        del graph[node]


def assignKcenter(nodes,kcenters,k):
    for i in nodes:
        kcenters[i]=k
    
def minDegree(graph):
    L=[]

    for v in graph.values():
            L.append(len(v))
    
    if (len(L)>0):
        return min(L)
    
def degeneresence (graph):
    kcenters={}

    maxdegree = []
    
    maxdegree.append(minDegree(graph))
    while(graph):
        if(len(maxdegree)!=0 and maxdegree[-1]<minDegree(graph)):
            maxdegree.append(minDegree(graph))

        L = nodesOfDegreeLessOrEqual(graph,maxdegree[-1])
        
        deleteNodes(graph,L)
        
        assignKcenter(L,kcenters,maxdegree[-1])


    kcenters = dict(sorted(kcenters.items()))
    return max(kcenters.values())+1,kcenters
        
def cleanfromD(D,neighbor,graph):
    K=-1
    
    for i in range(len(graph[neighbor])+1):
        if i in D and neighbor in D[i]:
            D[i].remove(neighbor)
            K=i
            break
    
    if K-1 in D:
        D[K-1].append(neighbor)
    else:
        D[K-1]=[neighbor]   
             
    return D   

def isDempty(D):
    for v in D.values():
        if len(v)!=0:return False
    return True

def clearDic(D):
    res = {k: v for k, v in D.items() if v!=[]}
    return res
    
def matulaandbeck(graph):
    '''
    -------------------------------------------------------------------TAKEN FROM WIKIPEDIA-----------------------------------------------------------------------------------------
    1-Initialize an output list L.
    2-Compute a number dv for each vertex v in G, the number of neighbors of v that are not already in L. Initially, these numbers are just the degrees of the vertices.
    3-Initialize an array D such that D[i] contains a list of the vertices v that are not already in L for which dv = i.
    4-Initialize k to 0.
    5-Repeat n times:!!!What's n?
    6-Scan the array cells D[0], D[1], ... until finding an i for which D[i] is nonempty.
    7-Set k to max(k,i)
    8-Select a vertex v from D[i]. Add v to the beginning of L and remove it from D[i].
    9-For each neighbor w of v not already in L, subtract one from dw and move w to the cell of D corresponding to the new value of dw.
    '''
    #1
    L=[]
    #2 et 3
    D={} 
    for k,v in graph.items():
        if len(v) not in D:
            D[len(v)]=[k]
        else:
            D[len(v)].append(k) 
    #4
    k=0
    #5 Not n times but while there's still nodes in D (same thing i guess)(well it's working like this too!)
    
    while(D):
        #6 no need to scan through D because with min(D), we get the min key with a value(node)
        
        i = min(D)

        #7   
        k=max(k,i)

        #8
        v = D[i][0]
        L.append(v)
        D[i].remove(v)
        
        #9
        for neighbor in graph[v]:
            if neighbor not in L:
                D=cleanfromD(D,neighbor,graph)
        
        #clear the dictionary from keys with empty values (Speed up the algorithm)
        D=clearDic(D)

        
        
                
        
    
                    
    
    return (k+1)
    

def opencsv(filename):
    f = open(filename, "r")
    L={}
    for x in f:
        #replace because last char of every line is an "\n" i don't really know why 
        a=x.replace('\n','').split(',')
        if len(a)>=2 and a[0].isdigit() and a[1].isdigit():
            if int(a[0]) in L:
                L[int(a[0])].append(int(a[1]))
            else:
                L[int(a[0])]=[int(a[1])]
            if int(a[1]) in L:
                L[int(a[1])].append(int(a[0]))
            else:
                L[int(a[1])]=[int(a[0])]
    return L


def opentxt(filename):
    f = open(filename, "r")
    L={}
    for x in f: 
        a=x.replace('\n','').split()
        if len(a)>=2 and a[0].isdigit() and a[1].isdigit():
            if int(a[0]) in L:
                L[int(a[0])].append(int(a[1]))
            else:
                L[int(a[0])]=[int(a[1])]
            if int(a[1]) in L:
                L[int(a[1])].append(int(a[0]))
            else:
                L[int(a[1])]=[int(a[0])]
    return L


def filetolist(filename):
    if filename[-3:]=='csv':L=opencsv(filename)
    else:L=opentxt(filename)
    return L
def main():
    # function calling
    
    #L is a test graph 
    L={}
    L[1]=[2,3,4,5,6]
    L[2]=[1,7]
    L[3]=[1,4,5]
    L[4]=[1,3,6]
    L[5]=[1,3,6,7]
    L[6]=[1,4,5,7,8,9,10]
    L[7]=[2,5,6,8]
    L[8]=[6,7,9]
    L[9]=[8,6]
    L[10]=[6]  
    ## ca-AstroPh.mtx 57
    ## ca-CondMat 26 
    ## delaunay_n14.mtx 5
    ##inf-power.mtx 6
    ##inf-USAIR97.mtx 27
    ##Stranke94.mtx 10
    
    graph = filetolist("ca-CondMat")
    graphMB = copy.deepcopy(graph)

    choix = 'False'
    while(choix!='0' and choix!='1' and choix!='2'and choix!='3'):
        choix = input("Pick :\n1- Base algorithm and Kcenters\n2- Matula & Beck Algorithm\n3- Both\n0- Exit\n")
    
    if choix=='1':
        degen,kcenters = degeneresence(graph)
        print("kcenters :",kcenters)
        print("Degeneracy :",degen)
    elif choix=='2':
        degenMB = matulaandbeck(graphMB)
        print("Matula & Beck Degeneracy :",degenMB)
    
    elif choix=='3':
        degen,kcenters = degeneresence(graph)
        print("kcenters :",kcenters)
        print("Degeneracy :",degen)
        degenMB = matulaandbeck(graphMB)
        print("Matula & Beck Degeneracy :",degenMB)
    elif choix=='0':exit()

    
    
    
    
    
    
    

# Main function calling
if __name__=="__main__":     
    main()