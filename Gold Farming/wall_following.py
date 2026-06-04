def generate_full_map_maze():
	clear()
	plant(Entities.Bush)
	use_item(Items.Weird_Substance, get_world_size() * 2**(num_unlocked(Unlocks.Mazes) - 1))


def rotate(d):
	first = d[0]
	d.remove(first)
	d.append(first)


def rotate_n(d, n):
	for i in range(n):
		rotate(d)


def wall_follow_step(directions):
	# directions = [left, forward, right, back]
	rotations = [3, 0, 1, 2]

	for i in range(4):
		if can_move(directions[i]):
			move(directions[i])
			rotate_n(directions, rotations[i])
			return


generate_full_map_maze()

directions = [West, North, East, South]

while True:
	if get_entity_type() == Entities.Treasure:
		harvest()
		generate_full_map_maze()
		directions = [West, North, East, South]

	wall_follow_step(directions)