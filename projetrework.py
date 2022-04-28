def nodesofdegreelessorequal(graph,degree):
    
    for k,v in graph.items():
        if degree>=len(v):
            return k
    return False

def deletenode(graph,node):

    for neighbor in graph[node]:
        if neighbor !=node:
            graph[neighbor].remove(node)

    del graph[node]

def degeneresence(graph):
    kcenters={}
    k=1
    while(graph):
        while(nodesofdegreelessorequal(graph,k)):
            
            node = nodesofdegreelessorequal(graph,k)
            #print(k,node,graph)
            deletenode(graph,node)
            kcenters[node]=k
            if not graph:return k,kcenters
        k+=1

    return k,kcenters
def matulaandbeck(graph):
    kcenters={}
    n=len(graph)
    L=[]
    G={}
    for k,v in graph.items():
        G[k]=len(v)
    #print(G)
    D={} 
    for k,v in graph.items():
        if len(v) not in D:
            D[len(v)]=[k]
        else:
            D[len(v)].append(k)
        
    #print(D)
    k=0
    #D=dict(sorted(D.items()))
    #print(D)
    #print(n)
    for j in range(n):
        for i in range(min(D),max(D)+1,1):
            
            if i in D and D[i]!=[]:
                k=max(k,i)
                L.insert(0,D[i][0])
                D[i].remove(D[i][0])
                for neighbor in graph[L[0]]:
                    if neighbor not in L:
                        D=cleanfromD(D,neighbor)
                break
        D=clearDic(D)
    #print(L,D)
    #print(len(L),len(graph))
                    
    
    print("Matula and beck",k+1)

def matulaandbeck(graph,kcenters):
    L={}
    G={}
    for k,v in graph.items():
        G[k]=len(v)
    D={} 
    for k,v in G.items():
        if v not in D:
            D[v]=[]
        D[v].append(k)
        
    print(G)
    D = dict(sorted(D.items()))
    print(D)
    k=0
    for j in range(n):
        i=0
        while(i not in D or len(D[i])==0):
            i+=1
        v=D[i][0]
        k=max(k,i)
        
        L.insert(0,v)

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


    
    graph = filetolist("test")
         
    
    degen,kcenters = degeneresence(graph)
    print("Degeneracy :",degen)
    print("kcenters :",kcenters)

# Main function calling
if __name__=="__main__":     
    main()