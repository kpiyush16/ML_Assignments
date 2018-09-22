import csv

knn_len = 6
def read_csv(fname):
	x, y = [], []
	with open(fname, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			x.append(list(map(int, row[:-1])))
			y.append(int(row[-1]))
	f.close()
	return (x, y)

if __name__ == '__main__':
	inputs, op = read_csv("data4.csv")
	examples = []
	with open("test4.csv") as t:
		reader = csv.reader(t)
		for row in reader:
			examples.append(list(map(int, row)))

	euclid, ans = [], []
	for ex in examples:
		for i in range(len(inputs)):
			euclid.append((sum(list(map(lambda a, b: (a-b)**2, ex, inputs[i]))), i))
		knn = sorted(euclid)[:knn_len]
		pos_examples = len([op[knn[i][1]] for i in range(knn_len) if op[knn[i][1]]])
		ans.append(int(pos_examples > knn_len-pos_examples))
		euclid = []
	ans = [str(x) for x in ans]
	print(" ".join(ans))