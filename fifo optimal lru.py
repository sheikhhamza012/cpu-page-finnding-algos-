def fifo(pagesize,inputString):
    q=[]
    pagefault=0
    while(len(inputString)>0):
        entery =inputString.pop(0)
        if(len(q)<pagesize and entery not in q):
            q.append(entery)
            pagefault+=1
        elif (len(q)==pagesize):
            if(entery not in q):
                pagefault+=1
                q.pop(0)
                q.append(entery)
    return pagefault

def optimal(pagesize,inputString):
    q=[]
    pagefault=0
    while(len(inputString)>0):
        entery =inputString.pop(0)
        if(len(q)<pagesize and entery not in q):
            q.append(entery)
            pagefault+=1
        elif (len(q)==pagesize and entery not in q):
                i=[inputString.index(i) if inputString.count(i)>0 else -1 for i in q ]
                j=i.index(-1) if i.count(-1)>0 else -1
                i = max(i)
                i=q.index(inputString[i])
                q[i if j<0 else j]=entery
                pagefault+=1
    return pagefault

def lru(pagesize,inputString):
    q=[]
    pagefault=0
    search=[]
    while(len(inputString)>0):
        entery =inputString.pop(0)
        search.append(entery)
        if(len(q)<pagesize and entery not in q):
            q.append(entery)
            pagefault+=1
        elif (len(q)==pagesize and entery not in q):
                i=[max([j for j,x in enumerate(search) if x==i]) for i in q]
                i = min(i)
                i=q.index(search[i])
                q[i]=entery
                pagefault+=1  
    return pagefault

pagesize=input("enter the page size: ")
arr=input("input the string: ")
arr=list(arr)
c=input("1-for fifo \n2-for optimal \n3-for lru\ninput: ")
if(c==1):
    print ("page fault ={}".format(fifo(pagesize,arr)))
elif(c==2):
    print ("page fault ={}".format(optimal(pagesize,arr)))
elif(c==3):
    print ("page fault ={}".format(lru(pagesize,arr)))

