def list_manipulation(n):
	r = [x for x in range(1, n+1)]
	print(r)
	done = r
	while True:
		r = r[::-1]
		print(r)
		for i in range(0, n-1, 2):
			r[i], r[i+1] = r[i+1], r[i]
		print(r)
		if r == done:
			break