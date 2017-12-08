#Mergesort Algorithms 

a = [6,4,1,1,5,9,3,75,75,43,7]

def sort(a):
	
	
	for x in xrange(len(a)):
		for y in xrange(len(a)-x-1):
			if a[y]<a[y+1] :
				temp = a[y]
				a[y]=a[y+1]
				a[y+1] = temp

	for x in xrange(len(a)-1):
			if a[x] != a[0]:
				return a[x]
				
			
	

	
print(sort(a))