def flatten(ls):
	new_ls=[]
	for n in range(len(ls)):
		if isinstance(ls[n],list):
			new_ls+=flatten(ls[n])
		else:
			new_ls.append(ls[n])
	return new_ls

print(flatten([2,9,[2,1,13,2],8,[2,6]]))
print(flatten([[9,[7,1,13,2],8],[7,6]]))
print(flatten([[9,[7,1,13,2],8],[2,6]]))
print(flatten([["this",["a",["thing"],"a"],"is"],["a","easy"]]))
print(flatten([]))