def find_frequency():
	result_frequency = 0
	final_result = -1
	frequency_results = [0]
	while (final_result == -1):
		with open("input.txt", "r") as file:
			for line in file:
				result_frequency += int(line)
				if result_frequency in frequency_results:
					final_result = result_frequency
					break;
				frequency_results.append(result_frequency)
	return final_result

def main():
	print(find_frequency())


if __name__ == '__main__':
    main()