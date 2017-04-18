import csv
csvoutput = open ('outputTest.csv', 'w')
csvfile = open('test.csv', 'r')
squarereader = csv.reader(csvfile, delimiter=",")
squarewriter = csv.writer(csvoutput, delimiter=",")
for row in squarereader:
	i = 0
	for i in range(0,4):
		if i == 0:
			squarewriter.writerow([str(row[0]), str(i+1), str(row[2]), str(row[3])])
		if i == 1:
			squarewriter.writerow([str(row[0]), str(i+1), str(int(row[2])+36), str(int(row[3]))])
		if i == 2:
			squarewriter.writerow([str(row[0]), str(i+1), str(int(row[2])+36), str(int(row[3])-36)])				
		if i == 3:
			squarewriter.writerow([str(row[0]), str(i+1), str(row[2]), str(int(row[3])-36)])				
			