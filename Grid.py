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
		
		self.top_left = current
	
	def get_pointer(self, x, y):
		#TODO
		return Grid_Pointer()
	
	def printable(self, wall_chr, node_chr, connector_chr):
		wc = str(wall_chr)[0]
		nc = str(node_chr)[0]
		cc = str(connector_chr)[0]
		nl = "\n"
		
		out = ""
		current = self.top_left
		line_start = current
		
		#Top wall
		out += wc * (self.xd * 2 + 1) + nl
		#Iterate down rows
		for y in range(self.yd):
			out += wc
			#Between nodes
			for x in range(self.xd):
				out += nc
				pass #TODO
			out += wc + nl
			#Between rows
			if y != self.yd - 1: #Skip last row, as it doesn't exist
				out += wc
				for x in range(self.xd):
					pass #TODO
				out += wc + nl
		#Bottom wall
		out += wc * (self.xd * 2 + 1)
		
		return out
		
		