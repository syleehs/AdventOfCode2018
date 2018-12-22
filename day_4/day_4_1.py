def sleepingTime():
	dict = createRecordsDict()
	peak_guard, peak_minutes, highest_total_sleep = 0, 0, 0
	for key in dict.keys():
		guard_sleep_total = 0
		guard_schedule = dict[key]
		for i in range(0, len(guard_schedule)):
			guard_sleep_total += guard_schedule[i]
		if highest_total_sleep < guard_sleep_total:
			highest_total_sleep = guard_sleep_total
			peak_guard = key
	guard_schedule = dict[peak_guard]
	
	for i in range(len(guard_schedule)):
		if guard_schedule[i] > peak_minutes:
			time = i
			peak_minutes = guard_schedule[i]
	return int(time)*int(peak_guard)

def createRecordsDict():
	dict = {}
	sorted_records=sortRecords()
	guard_id, sleep_start, sleep_end, old_guard_flag = 0, 0, 0, 0
	first_guard = 1
	for record_line in sorted_records:
		split_record=record_line.split(' ')
		key_string = split_record[2]
		if key_string == 'Guard':
			if first_guard == 1:
				first_guard = 0
			else:
				dict[guard_id] = sleep_schedule
			guard_id = (split_record[3].split('#'))[1]
			if guard_id in dict:
				sleep_schedule = dict[guard_id]
			else:
				sleep_schedule = [0 for x in range(60)]
		elif key_string == 'falls':
			sleep_start = int(split_record[1].split(':')[1].split(']')[0])
		elif key_string == 'wakes':
			sleep_end = int(split_record[1].split(':')[1].split(']')[0])
			for i in range(sleep_start, sleep_end):
				sleep_schedule[i] += 1
		else:
			return -1
	return dict

def sortRecords():
	records=[]

	with open("input.txt", "r") as file:
		for line in file:
			records.append(line)
	records.sort()
	return records

	return -1
	
def main():
	print("The result is: {}".format(sleepingTime()))
	

if __name__=='__main__':
	main()