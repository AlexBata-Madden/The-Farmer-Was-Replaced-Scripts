def farm_pumpkins():
	def go_to(x, y):
		while get_pos_x() != x:
			current = get_pos_x()

			east_distance = (x - current) % ws
			west_distance = (current - x) % ws

			if east_distance <= west_distance:
				move(East)
			else:
				move(West)

		while get_pos_y() != y:
			current = get_pos_y()

			north_distance = (y - current) % ws
			south_distance = (current - y) % ws

			if north_distance <= south_distance:
				move(North)
			else:
				move(South)


	def prepare_pumpkin_tile():
		if get_ground_type() != Grounds.Soil:
			till()

		if get_entity_type() != Entities.Pumpkin:
			plant(Entities.Pumpkin)


	def work_column():
		for _ in range(ws):
			prepare_pumpkin_tile()
			move(North)


	def pumpkin_id_if_ready():
		if get_entity_type() == Entities.Pumpkin and can_harvest():
			return measure()
		return -1


	def whole_field_ready():
		go_to(0, 0)
		id1 = pumpkin_id_if_ready()

		if id1 == -1:
			return False

		go_to(ws - 1, ws - 1)
		id2 = pumpkin_id_if_ready()

		return id1 == id2


	def pumpkin_worker():
		while True:
				work_column()


	def harvester_drone():
		go_to(ws-1,0)
 
		while True:
			work_column()

			if whole_field_ready():
				harvest()

	clear()

	ws = get_world_size()

	for _ in range(ws):
		spawn_drone(pumpkin_worker)
		move(East)

	harvester_drone()


farm_pumpkins()