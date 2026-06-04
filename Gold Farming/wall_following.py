def generate_full_map_maze():
	clear()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))

generate_full_map_maze()

directions = [West, North, East, South]

while True:
	heading = 0
	
	while get_entity_type() != Entities.Treasure:
		
		heading = (heading - 1) % 4
		
		while not move(directions[heading]):
			heading = (heading + 1) % 4
		
	harvest()
	generate_full_map_maze()