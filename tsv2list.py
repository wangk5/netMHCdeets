import sys
import csv

input_file = sys.argv[-1]

allele_doc = list(csv.reader(open(input_file, 'rU'), delimiter='\t'))
alleles = []
rando = []

for x in range (0, len(allele_doc[1])):
	if len(allele_doc[1][x]) < 2:
		rando.append(allele_doc[1][x])
	else:
		if allele_doc[1][x][1] == "*":
			alleles.append(allele_doc[1][x])

with open("allelelist", "w") as txt_file:
		y = len(alleles) - 1
		while y >= 0:
			txt_file.write("HLA-" + alleles[y] + "\n")
			y = y - 1
