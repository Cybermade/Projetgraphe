def nodesofdegreelessorequal(graph,degree):
    List=[]
    
    for k,v in graph.items():
        if degree>=len(v):
            List.append(k)
    
    return List

def deletenodes(graph,nodes):
    for node in nodes:
        
        for neighbor in graph[node]:
            if neighbor != node:
                while node in graph[neighbor]:
                    graph[neighbor].remove(node)
            #print(graph[neighbor],neighbor,node)
        del graph[node]


def assignkcenter(nodes,kcenters,k):
    for i in nodes:
        kcenters[i]=k
    
def mindegree(graph):
    L=[]

    for v in graph.values():
            L.append(len(v))
    
    if (len(L)>0):
        return min(L)
    
def degeneresence (graph):
    kcenters={}

    maxdegree = []
    
    maxdegree.append(mindegree(graph))
    while(graph):
        if(len(maxdegree)!=0 and maxdegree[-1]<mindegree(graph)):
            maxdegree.append(mindegree(graph))

        L = nodesofdegreelessorequal(graph,maxdegree[-1])
        
        deletenodes(graph,L)
        
        assignkcenter(L,kcenters,maxdegree[-1])


    kcenters = dict(sorted(kcenters.items()))
    return max(kcenters.values())+1,kcenters
        
def cleanfromD(D,neighbor):
    K=-1
    #print(neighbor)
    for k,v in D.items():
        if neighbor in v:
            D[k].remove(neighbor)
            K=k
    #print(K-1,neighbor)
    if K-1 in D:
        D[K-1].append(neighbor)
    else:
        D[K-1]=[neighbor]   
    #D=dict(sorted(D.items()))         
    return D   

def isDempty(D):
    for v in D.values():
        if len(v)!=0:return False
    return True

def clearDic(D):
    res = {k: v for k, v in D.items() if v!=[]}
    return res
def matulaandbeck(graph):
    L=[]
    G={}
    for k,v in graph.items():
        G[k]=len(v)
    
    D={} 
    for k,v in graph.items():
        if len(v) not in D:
            D[len(v)]=[k]
        else:
            D[len(v)].append(k)
        
    
    k=0
    
    while(D):
        i = min(D)
        v = D[i][0]
            
        k=max(k,i)
        L.insert(0,v)
        D[i].remove(v)
        for neighbor in graph[v]:
            if neighbor not in L:
                D=cleanfromD(D,neighbor)
        D=clearDic(D)
                
        
    #print(L,D)
    #print(len(L),len(graph))
                    
    
    print("Matula and beck",k+1)
    """
    D = dict(sorted(D.items()))
    print(D)
    k=0
    for j in range(n):
        i=0
        while(i not in D or len(D[i])==0):
            i+=1
        v=D[i][0]
        k=max(k,i)
        
        L.insert(0,v) """

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


    
    graph = filetolist("test.csv")
    matulaandbeck(graph)
    #print(graph)
    #degen,kcenters = degeneresence(graph)
    #print("Degeneracy :",degen)
    #print("kcenters :",kcenters)
    

# Main function calling
if __name__=="__main__":     
    main()