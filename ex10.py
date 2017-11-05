class Point:
	def __init__(self,x=0,y=0):
		self.x=x
		self.y=y


class Rectangle:
	def __init__(self,pos,w,h):
		self.corner=pos
		self.width=w
		self.height=h  
		
	def perimeter(self):
		return self.width*2+self.height*2

	def __str__(self):
		return  "({0}, {1}, {2})".format(self.corner, self.width, self.height)

	def flip(self):
		temp = self.width
		self.width=self.height
		self.height=temp


r = Rectangle(Point(),5,10)
print(r.perimeter())
print(r)
r.flip()
print(r)