import Node

class Grid:
	
	def __init__(self, xd, yd):
		self.xd = int(xd)
		self.yd = int(yd)
		if self.xd < 1 or self.yd < 1:
			raise ValueError("Grid dimensions must be one or greater.")
		
		#Make grid
		current = None
		line_start = None
		for y in range(self.yd):
			nn = Node()
			nn.set_bottom(line_start)
			current = nn
			line_start = nn
			for x in range(self.xd):
				nn = Node()
				nn.set_right(current)
				current = nn
		
		self.left_top = current