class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y
	def reflect_x(self):
		return Point(self.x,-self.y)


def distance(p1,p2):
	return ((p1.x-p2.x)**2+(p1.y-p2.y)**2)**0.5

print(distance(Point(1,1).reflect_x(),Point(1,2)))
