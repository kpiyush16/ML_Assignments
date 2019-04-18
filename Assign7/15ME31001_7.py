import numpy as np
import csv
import random

def euclidean(x, y):
	su=0
	for i, j in zip(x, y):
		su += (i-j)**2
	return su

def K_Means(k, data, iterations):
	clusters = [x+1 for x in range(k)]
	leng = len(data)
	cent = random.sample(range(leng), k)
	tup = {x: data[y] for (x, y) in zip(clusters, cent)}
	data_labels = [(0, t) for t in data]
	data_labels_new = []
	it = 0
	while(it < iterations):
		it += 1
		for pts in data_labels:
			tmp = []
			for d in tup:
				tmp.append((euclidean(tup[d], pts[1]), d))
			clus = sorted(tmp)[0][1]
			data_labels_new.append((clus, pts[1]))
		data_labels = data_labels_new
		tmp_dct = {}

		# Updating Centroid
		for i in data_labels:
			if not i[0] in tmp_dct:
				tmp_dct[i[0]] = [i[1], 1]
			else:
				tmp_dct[i[0]][0] = map(sum, zip(tmp_dct[i[0]][0], i[1]))
				tmp_dct[i[0]][1] += 1
		for d in tup:
			div = tmp_dct[d][1]
			tup[d] = [x / div for x in tmp_dct[d][0]]
		data_labels_new = []
		
	# Final Centroid with position
	# print(tup)
	return(data_labels)

if __name__ == '__main__':
	with open("data7.csv", "r") as f:
		reader = csv.reader(f)
		inp = []
		for row in reader:
			inp.append(list(map(int, row)))
	ans = K_Means(k=2, data=inp, iterations=10)
	ans = [str(x[0]) for x in ans]
	ans = " ".join(ans)
	print(ans)
	with open("15ME31001_7.out", "w") as t:
		t.write(ans)

