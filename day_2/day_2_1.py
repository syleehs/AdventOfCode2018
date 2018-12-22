def checksumIDs():
	count_2 = 0
	count_3 = 0
	with open("input.txt", "r") as file:
		for line in file:
			track_2 = 0
			track_3 = 0
			for i in range(len(line)):
				repeat_char_count = line.count(line[i])
				if (repeat_char_count == 2 and track_2 == 0):
					count_2+=1
					track_2+=1
				elif (repeat_char_count == 3 and track_3 == 0):
					count_3+=1
					track_3+=1
	return count_2*count_3

def main():
	print(checksumIDs())

if __name__ == '__main__':
	main()