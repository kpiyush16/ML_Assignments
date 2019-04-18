import numpy as np
import csv

class Perceptron(object):
	def __init__(self, no_of_inputs, epochs=10, learning_rate=0.1):
		self.epochs = epochs
		self.learning_rate = learning_rate
		self.weights = np.random.random_sample(no_of_inputs + 1)
   
	def predict(self, inputs):
		return 1/(1 + np.exp((-1)*(np.dot(inputs, self.weights[1:]) + self.weights[0])))

	def train(self, training_inputs, labels):
		for _ in range(self.epochs):
			loss = 0
			for inputs, label in zip(training_inputs, labels):
				prediction = self.predict(inputs)
				loss += (label - prediction)**2
				# print(prediction, label, inputs)
				self.weights[1:] -= self.learning_rate * (label - prediction) * inputs * prediction * (1 - prediction)
				self.weights[0] -= self.learning_rate * (label - prediction)
			loss /= 2*len(training_inputs)
			# print(loss)
			# print(self.weights)
def read_csv(fname):
	x, y = [], []
	with open(fname, 'r') as f:
		reader = csv.reader(f)
		for row in reader:
			x.append(list(map(np.float, row[:-1])))
			y.append(np.float(row[-1]))
	f.close()
	return (x, y)
if __name__ == '__main__':
	inp, op = read_csv("data6.csv")
	inp = np.array(inp)
	per = Perceptron(len(inp[0]))
	per.train(inp, op)
	examples, ans = [], []
	with open("test6.csv") as t:
		reader = csv.reader(t)
		for row in reader:
			examples.append(list(map(int, row)))
	for ex in examples:
		ans.append(str(int(round(per.predict(ex), 1))))
	print(" ".join(ans))
	with open("15ME31001_6.out", "w") as t:
		t.write(" ".join(ans))

