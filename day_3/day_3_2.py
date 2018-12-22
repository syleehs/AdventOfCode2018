def overlapFabric():
	fabric_sheet = [[0 for x in range(1000)] for y in range(1000)] 
	intact_fabric = []

	with open("input.txt", "r") as file:
		for line in file:
			flag = 0
			fabric_claim = line.split(' ')
			id = fabric_claim[0]
			start_location = [int(x) for x in (fabric_claim[2])[:-1].split(',')]
			fabric_dimension = [int(x) for x in fabric_claim[3].strip().split('x')]
			for x in range(start_location[0], start_location[0] + fabric_dimension[0]):
				for y in range(start_location[1], start_location[1] + fabric_dimension[1]):
					if fabric_sheet[x][y] == 0:
						fabric_sheet[x][y] = id
					else:
						if fabric_sheet[x][y] in intact_fabric:
							intact_fabric.remove(fabric_sheet[x][y])
						fabric_sheet[x][y] = id
						flag = 1
			if flag == 0:
				intact_fabric.append(id)
	return intact_fabric

	
	
def main():
	print(overlapFabric())

if __name__ == '__main__':
	main()