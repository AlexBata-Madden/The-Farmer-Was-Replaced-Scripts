def farm_pumpkins():
	
	def go_to(x, y):
		size = get_world_size()

		while get_pos_x() != x:
			current = get_pos_x()
	
			east_distance = (x - current) % size
			west_distance = (current - x) % size
	
			if east_distance <= west_distance:
				move(East)
			else:
				move(West)
	
		while get_pos_y() != y:
			current = get_pos_y()
	
			north_distance = (y - current) % size
			south_distance = (current - y) % size
	
			if north_distance <= south_distance:
				move(North)
			else:
				move(South)
			
		
	def harvester_drone():
		ws = get_world_size()
			
		while True:
			for _ in range(ws):
				if get_ground_type() != Grounds.Soil:
					till()

				y = get_pos_y()

				if get_entity_type() == Entities.Dead_Pumpkin:
					harvest()
				
				plant(Entities.Pumpkin)
				move(North)
			go_to(31,31)
			if(can_harvest() and get_entity_type() == Entities.Pumpkin):
				id1 = measure()
			else:
				id1 = -1
			go_to(0,0)
			if(can_harvest() and get_entity_type() == Entities.Pumpkin):
				id2 = measure()
			else:
				id2 = -2
			if id1 == id2:
				harvest()
			go_to(31,0)
			
				
	def pumpkin_worker():
		ws = get_world_size()
			
		while True:
			for _ in range(ws):
				if get_ground_type() != Grounds.Soil:
					till()

				y = get_pos_y()

				if get_entity_type() == Entities.Dead_Pumpkin:
					harvest()
				
				plant(Entities.Pumpkin)
				move(North)
	
	clear()
	
	for _ in range(max_drones() - 1):
		if spawn_drone(pumpkin_worker):
			move(East)
	
	harvester_drone()
	
farm_pumpkins()