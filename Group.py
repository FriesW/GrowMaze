class Group:

	def __init__(self, dictionary, array):
		self.groups = array
		self.groups.append(self) #List of all groups
		self.lookup = dictionary #Reverse node to group lookup
		
		self.all = []
		self.live = []
	
	def add(self, node):
		if node not in self.all:
			self.lookup[node] = self
			self.all.append(node)
	
	def add_live(self, node):
		self.add(node)
		if node not in self.live:
			self.live.append(node)
		
		def trim_from_node(node, recurse):
			#If all bordering nodes are in group, then node is dead
			total = len(node.get_nodes())
			for n in node.get_nodes():
				if n in self.lookup and self.lookup[n] == self:
					total -= 1
					if recurse:
						trim_from_node(n, False)
			if total == 0:
				self.live.pop( self.live.index(node) )
		
		trim_from_node(node, True)
	
	def get_all_live(self):
		return self.live[:]
	
	def total_all_nodes(self):
		return len(self.all)
	
	def get_all(self):
		return self.all[:]
	
	def total_live_nodes(self):
		return len(self.live)
	
	def get_live_node(self, index):
		return self.live[index]
	
	
	
		