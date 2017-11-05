text = open("test.txt")
lines = text.readlines()
for n in lines:
	if n.find('snake')!=-1:
		print(n,end='')