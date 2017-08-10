from Node import Node

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
			if line_start != None:
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
		do = True
		while do:
			out += wc
			#Between nodes
			while current.has_right_node():
				out += nc
				if current.is_right_connected():
					out += cc
				else:
					out += wc
				current = current.get_right_node()
			out += nc + wc + nl
			
			#Between rows
			current = line_start
			if line_start.has_bottom_node(): #Last row case
				while current.has_right_node():
					out += wc
					if current.is_bottom_connected():
						out += cc
					else:
						out += wc
					current = current.get_right_node()
				#Last node in row
				if current.is_bottom_connected():
					out += cc
				else:
					out += wc
				out += wc + nl
			
			#Next row of NODES
			do = line_start.has_bottom_node()
			if do:
				current = line_start.get_bottom_node()
				line_start = current
			
		#Bottom wall
		out += wc * (self.xd * 2 + 1)
		
		return out
		
		