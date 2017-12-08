
a = [6,4,1]

def mergesort(a):
    n = len(a)
    
    if n < 2 :
      return a
    mid = n/2
    left = []
    right = []
    j = 0
    for i in range(mid):
        left.append(a[i])
    for j in range(mid):
        right.append(a[mid+j])
    print("left:", left)
    mergesort(left)
    print("right ",right)
    mergesort(right)
    merge(left,right,a)
def merge(l,r,a):
    nl = len(l)
    nr = len(r)
    i=j=k=0
    print("merge left",l)
    print("merge right",r)
    while i<nl and j<nr:
        if(l[i] <= r[j]):
            a[k] = l[i]
            i+=1
        else :
            a[k] = r[j]
            j+=1
        k+=1
    
    while i<nl:
        a[k] = l[i]
        i+=1
        k+=1
    
    while j<nr:
        a[k] = r[j]
        j+=1
        k+=1
    
mergesort(a)

for i in range(len(a)):
    print ("%d" %a[i]),