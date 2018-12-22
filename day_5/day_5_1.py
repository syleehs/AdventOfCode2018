def reducePolymer():
	with open("input.txt", "r") as file:
		i = 0
		for line in file:
			polymer_composition = list(line)
		while (i < len(polymer_composition)-1):
			if ((polymer_composition[i].islower() and polymer_composition[i].upper() == polymer_composition[i+1]) or (polymer_composition[i].isupper() and polymer_composition[i].lower() == polymer_composition[i+1])):
				del polymer_composition[i]
				del polymer_composition[i]
				if i > 0:
					i -=1
			else:
				i+=1
	return polymer_composition

	
def main():
	print("The result is: {}".format(len(reducePolymer())))
	

if __name__=='__main__':
	main()