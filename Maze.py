from Param_Utils import *
from Grid import Grid
from Group_Manager import Group_Manager
import random

master = Grid(7,7)

def hash_maze(hash):
	l = decode(hash)
	make_maze(l[0], l[1], l[2], l[3])

def make_maze(xd, yd, sp, seed):
	xd = int(xd)
	yd = int(yd)
	sp = int(sp)
	seed = sanitize_seed(seed)
	
	random.seed(seed)
	
	#master = Grid(xd, yd)
	
	#Select starting points for growth
	starting_points = []
	while len(starting_points) < sp:
		candidate = (random.randrange(0,xd), random.randrange(0,yd))
		if candidate not in starting_points:
			starting_points.append(candidate)
	
	#Create groups
	gm = Group_Manager()
	for x, y in starting_points:
		gm.make_group( master.get_node(x, y) );
	
	#while gm.get_group(0).total_live_nodes() > 0:
	while gm.get_group(0).total_all_nodes() < xd * yd:
		print "Cycle"
		g = gm.get_group( random.randrange( gm.total_groups() ) )
		#Every group will always have live nodes, until there is one group
		print "Picking one of", g.total_live_nodes(), "live nodes"
		rand = random.randrange( g.total_live_nodes() )
		print "Picking node", rand
		sn = g.get_live_node(rand)
		print sn, "was picked"
		#sn = g.get_live_node( random.randrange( g.total_live_nodes() ) ) #source node
		cns = sn.get_unconnected_nodes() #candidate nodes
		random.shuffle(cns)
		print "Found", len(cns), "candidate nodes"
		
		done = False
		while not done and len(cns) > 0:
			cn = cns.pop(0) #candidate node
			if not gm.node_in_group(cn):
				sn.connect_to(cn)
				g.add_live(cn)
				done = True
				print "Added node to group"
			elif g != gm.get_group_by(cn):
				sn.connect_to(cn)
				gm.combine_groups(g, gm.get_group_by(cn))
				done = True
				print "Combined two groups"
		
		if done:
			pass
			#Here we need to remove nodes which are no longer live from group g
		
	print master.printable()


make_maze(7,7,3,"Apples")
	
'''	
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
			
	
	random.randrange'''
