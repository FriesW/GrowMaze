class Node:

	__t = 0
	__r = 1
	__b = 2
	__l = 3
	
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
			print "Error: no node assigned"
			return
		self.connects[dir] = True
		self.nodes[dir].connects[self.__inverse[dir]] = True
	
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