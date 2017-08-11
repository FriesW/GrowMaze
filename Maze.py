from Grid import Grid
from Param_Utils import sanitize_seed
from Group_Manager import Group_Manager
import random

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
	gm = Group_Manager()
	for x, y in starting_points:
		gm.make_group( master.get_node(x, y) );
	
	#while gm.get_group(0).total_live_nodes() > 0:
	while gm.get_group(0).total_all_nodes() < xd * yd:
		g = gm.get_group( random.randrange( gm.total_groups() ) )
		#Every group will always have live nodes, until there is one group
		sn = g.get_live_node( random.randrange( g.total_live_nodes() ) ) #source node
		cns = sn.get_unconnected_nodes() #candidate nodes
		random.shuffle(cns)
		
		done = False
		while not done and len(cns) > 0:
			cn = cns.pop(0) #candidate node
			if not gm.node_in_group(cn):
				sn.connect_to(cn)
				g.add_live(cn)
				done = True
			elif g != gm.get_group_by(cn):
				sn.connect_to(cn)
				gm.combine_groups(g, gm.get_group_by(cn))
				done = True
	
	return master.printable()
