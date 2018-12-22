def commonLetters():
	mistakes_allowed = 1
	with open("input.txt", "r") as file:

		boxIDs = [line.strip() for line in file]
		num_lines = len(boxIDs)
		size_of_string = len(boxIDs[0])

		for current_index in range(num_lines):
			for next_index in range(current_index + 1, num_lines):
				for i in range(size_of_string):
					if ((boxIDs[current_index])[i] != (boxIDs[next_index])[i]):
						mistakes_allowed -= 1
						if (mistakes_allowed == -1): break
				if (mistakes_allowed >= 0):
					return findCommonLetters((boxIDs[current_index]), (boxIDs[next_index]), size_of_string)
				mistakes_allowed = 1
	return -1

def findCommonLetters(current_string, next_string, size_of_string):
	result = ''
	for i in range(size_of_string):
		if (current_string[i] == next_string[i]):
			result += current_string[i]
	return result
	
def main():
	print(commonLetters())

if __name__ == '__main__':
	main()