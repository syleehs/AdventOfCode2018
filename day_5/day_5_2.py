ALPHABET = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

def reducePolymer():
	for letter in ALPHABET:
		with open("input.txt", "r") as file:
			i = 0
			for line in file:
				polymer_composition = list(line)
				polymer_composition = list(filter(lambda a: a != letter, polymer_composition))
				polymer_composition = list(filter(lambda a: a != letter.upper(), polymer_composition))
		while (i < len(polymer_composition)-1):
			if ((polymer_composition[i].islower() and polymer_composition[i].upper() == polymer_composition[i+1]) or (polymer_composition[i].isupper() and polymer_composition[i].lower() == polymer_composition[i+1])):
				del polymer_composition[i]
				del polymer_composition[i]
				if i > 0:
					i -=1
			else:
				i+=1
		if letter == 'a':
			shortest_len = len(polymer_composition)
		elif shortest_len > len(polymer_composition):
			shortest_len = len(polymer_composition)
	return shortest_len

	
def main():
	print("The result is: {}".format(reducePolymer()))
	

if __name__=='__main__':
	main()