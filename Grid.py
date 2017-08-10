from Node import Node
from Pointer import Pointer

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
	
	def get_pointer(self, x = 0, y = 0):
		p = Pointer(self.top_left, self.xd, self.yd)
		p.goto(x, y)
		return p
	
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
			for x in range(self.yd):
				#Row - down nodes
				row1 = wc
				
				pass
				
				row1 += wc + nl
				
				#Row - between nodes
				row2 = ""
				if y != self.yd - 1: #Last row case
					row2 = wc
					pass
					row2 += wc + nl
				
				out += row1 + row2
				
		#Bottom wall
		out += wc * (self.xd * 2 + 1)
		return out
		
		
		
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