def convert_file(source, destination):
	file = open(source)
	content = file.read()
	data = content.split("\n")[5:]
	delta_t = 1.000000E-8
	conv = [row.replace(",", ".").split() for row in data] 
	nice_table = []
	try:
		for i, row in enumerate(conv):
			if len(row) > 5:
				entry = []
				entry.append(delta_t * i)
				entry.append(row[2])
				entry.append(row[5])
				nice_table.append(entry)
	except Exception, e:
		print e
		print len(nice_table)
	output_file = open(destination, "w")
	new_content = "\n".join([str(row[0]) + ",\t" + str(row[1]) + 
				",\t" + str(row[2]) for row in nice_table])

	output_file.write(new_content)

def main():
	source = raw_input("Jaki plik uzyc? ")
	destination = raw_input("Gdzie zapisac? ")
	convert_file(source, destination)

if __name__ == "__main__":
	main()