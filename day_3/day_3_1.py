def overlapFabric():
	fabric_sheet = [[0 for x in range(1000)] for y in range(1000)] 
	overlapped_fabric_count = 0

	with open("input.txt", "r") as file:
		for line in file:
			fabric_claim = line.split(' ')
			start_location = [int(x) for x in (fabric_claim[2])[:-1].split(',')]
			fabric_dimension = [int(x) for x in fabric_claim[3].strip().split('x')]

			fabric_sheet, overlapped_fabric_count = fillFabricSheet(fabric_sheet, start_location, fabric_dimension, overlapped_fabric_count)

	return overlapped_fabric_count

def fillFabricSheet(fabric_sheet, start_location, fabric_dimension, overlapped_fabric_count):
	for x in range(start_location[0], start_location[0] + fabric_dimension[0]):
		for y in range(start_location[1], start_location[1] + fabric_dimension[1]):
			if fabric_sheet[x][y] == 0:
				fabric_sheet[x][y] = 1
			elif fabric_sheet[x][y] == 1:
				fabric_sheet[x][y] = 2
				overlapped_fabric_count += 1
	return fabric_sheet, overlapped_fabric_count
	
def main():
	print(overlapFabric())

if __name__ == '__main__':
	main()