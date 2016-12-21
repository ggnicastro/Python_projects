samplemap = {}
i = 0
num_samples = int(raw_input("Number of samples? "))
i = 1
for i in range(1, num_samples+1):
	name = raw_input("What is the sample name " + str(i) + "? ")
	output = raw_input("name path " + str(i) +"? ")
	samplemap[i] = (name + output)
	i += 1
	print samplemap[i]


