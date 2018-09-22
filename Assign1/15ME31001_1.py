# Piyush Khushlani
# 15ME31001
# Assignment 1
import csv
import sys
x, y = [], []
with open (sys.argv[-1], 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		x.append(list(map(int, row[:-1])))
		y.append(int(row[-1]))

# Separating positives and negatives
pos, neg = [a for (a, b) in zip(x, y) if (b == 1)], [a for (a, b) in zip(x, y) if (b == 0)]
cols = [[pos[i][j] for i in range(len(pos))] for j in range(len(pos[0]))]
fea = [None if (all(cols[i]) != any(cols[i])) else (1 if all(cols[i]) else (-1)) for i in range(len(cols))]
features = [fea[i]*(i+1) for i in range(len(fea)) if (fea[i] != None)]

for i in neg:
	tmp = 1
	for x in features:
		if(x > 0):
			tmp = tmp and i[x-1]
		else:
			tmp = tmp and not i[(-1)*(x+1)]
	if(tmp != 0):
		print(0)
		exit()
features = [str(len(features))]+[str(b) for b in features]
print(", ".join(features))