class Node:

	__t = 0
	__r = 1
	__b = 2
	__l = 3
	
	__all     = [__t, __r, __b, __l]
	__inverse = [__b, __l, __t, __r]

	def __init__(self):
		self.nodes = self.__init_array(4, None)
		self.connects = self.__init_array(4, False)
		
	def __init_array(self, l, v):
		a = []
		for i in range(l):
			a.append(v)
		return a
		
	def __set_node(self, node, dir):
		self.nodes[dir] = node
		node.nodes[self.__inverse[dir]] = self
	
	def __connect_node(self, dir):
		if self.nodes[dir] == None:
			raise IndexError("There is no node to connect to.")
		self.connects[dir] = True
		self.nodes[dir].connects[self.__inverse[dir]] = True
	
	def __has_node(self, dir):
		return self.nodes[dir] != None
	
	def __is_connected(self, dir):
		return self.connects[dir]
	
	def __get_node(self, dir):
		if not self.__has_node(dir):
			raise IndexError("Node doesn't exist! First check if it does with is_DIR_node().");
		return self.nodes[dir]
	
	def set_top(self, node):
		self.__set_node(node, self.__t)
		
	def set_right(self, node):
		self.__set_node(node, self.__r)
		
	def set_bottom(self, node):
		self.__set_node(node, self.__b)
		
	def set_left(self, node):
		self.__set_node(node, self.__l)
	
	def connect_top(self):
		self.__connect_node(self.__t)
		
	def connect_right(self):
		self.__connect_node(self.__r)
		
	def connect_bottom(self):
		self.__connect_node(self.__b)
		
	def connect_left(self):
		self.__connect_node(self.__l)
		
	def has_top_node(self):
		return self.__has_node(self.__t)
	
	def has_right_node(self):
		return self.__has_node(self.__r)
	
	def has_bottom_node(self):
		return self.__has_node(self.__b)
	
	def has_left_node(self):
		return self.__has_node(self.__l)
	
	def is_top_connected(self):
		return self.__is_connected(self.__t)
	
	def is_right_connected(self):
		return self.__is_connected(self.__r)
	
	def is_bottom_connected(self):
		return self.__is_connected(self.__b)
	
	def is_left_connected(self):
		return self.__is_connected(self.__l)
	
	def get_top_node(self):
		return self.__get_node(self.__t)
	
	def get_right_node(self):
		return self.__get_node(self.__r)
	
	def get_bottom_node(self):
		return self.__get_node(self.__b)
	
	def get_left_node(self):
		return self.__get_node(self.__l)
	
	def get_nodes(self):
		out = []
		for n in self.nodes:
			if n != None:
				out.append(n)
		return out
	
	def is_set_to(self, node):
		return node in self.nodes
	
	def is_connected_to(self, node):#Not used
		if node not in self.nodes:
			return False
		return self.connects[self.nodes.index(node)]
	
	def get_connected_nodes(self):
		out = []
		for i in range(4):
			if self.nodes[i] != None and self.connects[i] == True:
				out.append(self.nodes[i])
		return out
	
	def get_unconnected_nodes(self):
		out = []
		for i in range(4):
			if self.nodes[i] != None and self.connects[i] == False:
				out.append(self.nodes[i])
		return out
	
	def connect_to(self, node):
		if node not in self.nodes:
			raise IndexError("There is no node to connect to.")
		self.__connect_node(self.nodes.index(node))