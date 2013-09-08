# this is my exercise number 15 in python 
tmp=[]
for i in range(0,21): # problems in python whit multidimensional arrays, :C 
	tmp_a=[]
	for j in range(0,21):
		tmp_a.append(-1)
	tmp.append(tmp_a)


# recursion: the sum of the previous paths. memorization for the fast proccess of paths, tmp[x][y]

def count_paths(x,y):
	if tmp[x][y]>0:
		return tmp[x][y]
	if y == 0 or x == 0:
		return 1
	a = count_paths(x-1,y)
	b = count_paths(x,y-1)
	tmp[x][y]=a+b
	return tmp[x][y]



print count_paths(20,20)