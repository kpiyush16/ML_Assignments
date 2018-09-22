# Roll			Name    				Assignment Number
# 15ME31001		Piyush Khushlani		3
# To be executed in python 3

import csv

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
	inputs, op = read_csv("data3.csv")
	# print(inp, op)
	# print("outputs", op)
	cols = [[inputs[j][i] for j in range(len(inputs))] for i in range(len(inputs[0]))]
	pr = len([x for x in op if x])/len(op)
	probs, prob_class = [], (round(pr, 4),round((1-pr), 4))
	# print(prob_class)
	for col in cols:
		# print("column", col)
		pair = list(zip(col, op))
		out_pos, out_neg = [x[0] for x in pair if (x[1])], [x[0] for x in pair if (not x[1])]
		# print("Pos and neg")
		# print(out_pos, out_neg)
		p_pos, p_neg = (len([x for x in out_pos if x])+1)/(len(out_pos)+2), (len([x for x in out_neg if x])+1)/(len(out_neg)+2)
		# print((round(p, 4),round((1-p), 4)))
		probs.append([(round(p_pos, 4),round((1-p_pos), 4)), (round(p_neg, 4),round((1-p_neg), 4))])
	# print(probs)
	examples = []
	with open("test3.csv") as t:
		reader = csv.reader(t)
		for row in reader:
			examples.append(list(map(int, row)))
	# print(examples)
	res = []
	for ex in examples:
		cond_pos = 1
		cond_neg = 1
		for i, val in enumerate(ex):
			cond_pos *= probs[i][0][1-val]
			cond_neg *= probs[i][1][1-val]
		# print(cond_pos, cond_neg)
		like_pos = cond_pos*prob_class[0]
		like_neg = cond_neg*prob_class[1]
		total = like_pos + like_neg
		final1 = (like_pos)/(total)
		final2 = (like_neg)/(total)
		res.append(int(final1>final2))
	res = [str(x) for x in res]
	print(" ".join(res))
