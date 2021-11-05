def add(a,b):
	i=0
	sum=0
	E=[]
	while i<len(a) and len(b):
		sum=a[i]+b[i]
		E.append(sum)
		i=i+1
	print(E)
n=[7,6,8,9,7]
m=[4,7,5,6,5]
add(n,m)