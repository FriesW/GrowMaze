from Param_utils import *
from Grid import Grid
import random

def hash_maze(hash):
	l = decode(hash)
	make_maze(l[0], l[1], l[2], l[3])

def make_maze(xd, yd, sp, seed):
	xd = int(xd)
	yd = int(yd)
	sp = int(sp)
	seed = sanitize_seed(seed)
	
	random.seed(seed)
	
	master = Grid(xd, yd)
	
	#Select starting points for growth
	starting_points = []
	while len(starting_points) < sp:
		candidate = (random.randrange(0,xd), random.randrange(0,yd))
		if candidate not in starting_points:
			starting_points.append(candidate)
	
	#Create groups
	groups = [] #groups[groupnumber][all_nodes|live_nodes]
	for x, y in starting_points:
		groups.append( [ [master.get_node(x, y)], [master.get_node(x, y)] ])
	
	#Begin growth
	while len(groups[0][1]) > 0: #Continue untill no nodes are alive
		#For every group of nodes
		for all_nodes, live_nodes in groups:
			#For every live node
			for node in live_nodes:
				#Every unconnected node has a 1% chance
				for candidate in node.get_unconnected_nodes():
					#Prevent self linking
					if candidate not in all_nodes:
						#1% chance
						if random.randrange(100) == 0:
							#Growth!
							candidate.connect_to(node)
							#Look for overlap with another group
							for i in range(len(groups)):
								other_all, other_live = groups[i]
								if candidate in other_all:
									all_nodes.extend(other_all)
									live_nodes.extend(other_live)
								
							for other_all, other_live in groups:
								if candidate in other_all:
									
									
							#Add candidate
							all_nodes.append(candidate)
							live_nodes.append(candidate)
	def consider_group(
			
	
	random.randrange