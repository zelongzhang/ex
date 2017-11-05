def turn_clockwise(direction):
	if direction=='N' or direction =='n':
		return 'E'
	elif direction=='E' or direction =='e':
		return 'S'
	elif direction=='S' or direction =='s':
		return 'W'
	elif direction=='W' or direction =='w':
		return 'N'
	else:
		return


def grade(mark):
	if mark>=75:
		return('First')
	elif mark>=70 and mark<75:
		return('Upper Second')
	elif mark>=60 and mark<70:
		return('Second')
	elif mark>=50 and mark<60:
		return('Third')
	elif mark>=45 and mark<50:
		return('F1 Supp')
	elif mark>=40 and mark<45:
		return('F2')
	else:
		return('F3')


while True:
	print(turn_clockwise(str(input('Enter a direction\n'))))
	print(grade(float(input('Enter a mark\n'))))