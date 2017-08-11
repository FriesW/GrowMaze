from Node import Node

class Grid:
	
	def __init__(self, xd, yd):
		self.xd = int(xd)
		self.yd = int(yd)
		if self.xd < 1 or self.yd < 1:
			raise ValueError("Grid dimensions must be one or greater.")
		
		def make_line(length):
			first = Node()
			current = first
			for x in range(length - 1):
				current.set_right( Node() )
				current = current.get_right_node()
			return first
		
		def zip_lines(top, bottom):
			while top.has_right_node() and bottom.has_right_node():
				top.set_bottom(bottom)
				top = top.get_right_node()
				bottom = bottom.get_right_node()
			top.set_bottom(bottom)
		
		#Make grid
		self.top_left = make_line(self.xd)
		row_old = self.top_left
		for i in range(self.yd - 1):
			row_new = make_line(self.xd)
			zip_lines(row_old, row_new)
			row_old = row_new
	
	def get_node(self, x, y):
		if x < 0 or x >= self.xd or\
			y < 0 or y >= self.yd:
			raise IndexError("That position is outside of the grid boundaries.")
		current = self.top_left
		for i in range(x):
			current = current.get_right_node()
		for i in range(y):
			current = current.get_bottom_node()
		return current
	
	def printable(self, wall_chr = u"\u2588", node_chr = ' ', connector_chr = ' ',\
						horizontal_scale = 3):
		hs = int(horizontal_scale)
		if type(wall_chr) != unicode:
			wall_chr = str(wall_chr)
		wc = wall_chr[0] * hs
		if type(node_chr) != unicode:
			node_chr = str(node_chr)
		nc = node_chr[0] * hs
		if type(connector_chr) != unicode:
			connector_chr = str(connector_chr)
		cc = connector_chr[0] * hs
		nl = "\n"
		
		out = ""
		current = self.top_left
		line_start = current
		
		#Top wall
		out += wc * (self.xd * 2 + 1) + nl
		#Iterate down rows
		for y in range(self.yd):
			#Iterate horizontally across nodes
			row1 = ""
			row2 = ""
			for x in range(self.xd):
				#Row - down nodes
				row1 += nc
				if current.is_right_connected():
					row1 += cc
				else:
					row1 += wc
				
				#Row - between nodes
				if current.has_bottom_node(): #Last row case
					row2 += wc
					if current.is_bottom_connected():
						row2 += cc
					else:
						row2 += wc
				
				if current.has_right_node():
					current = current.get_right_node()
			
			out += wc + row1 + nl
			
			if current.has_bottom_node():
				line_start = line_start.get_bottom_node()
				current = line_start
				
				out += row2 + wc + nl
				
		#Bottom wall
		out += wc * (self.xd * 2 + 1)
		return out