n=int(input())
r=[x for x in range(n)]
d=r
while True:
	r=r[::-1]
	for i in range(0,n-1,2):
		r[i],r[i+1]=r[i+1],r[i]
	pring(r)
	if r==d:
		break