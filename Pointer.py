class Pointer:
	
	def __init__(self, top_left_node, x, y):
		self.origin = top_left_node #For duplicating pointer
		self.cn = top_left_node #current node
		self.cx = 0 #current x
		self.cy = 0 #current y
		self.mx = x - 1 #max x
		self.my = y - 1 #max y
		
	def goto(self, x, y):
		x = int(x)
		y = int(y)
		self.move(x - self.cx, y - self.cy)
	
	def move(self, x, y):
		x = int(x)
		y = int(y)
		self.cx += x
		self.cy += y
		if self.cx < 0 or self.cx > self.mx or\
			self.cy < 0 or self.cy > self.my:
			raise IndexError("Out of bounds.")
		for i in range(abs(x)):
			if x > 0:
				self.cn = self.cn.get_right_node()
			else:
				self.cn = self.cn.get_left_node()
		for i in range(abs(y)):
			if y > 0:
				self.cn = self.cn.get_bottom_node()
			else:
				self.cn = self.cn.get_top_node()
		
	
	def get_node(self):
		return self.cn