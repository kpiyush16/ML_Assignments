# Roll			Name    				Assignment Number
# 15ME31001		Piyush Khushlani		2

import math
import csv

class Node():
    def __init__(self, parent=None, value=None, is_leaf=False):
        self.parent = parent
        self.value = value
        self.left = None
        self.right = None
        self.is_leaf = is_leaf

def read_csv(fname):
    x, y = [], []
    with open(fname, 'r') as f:
        reader = csv.reader(f)
        for row in reader:
            x.append(list(map(int, row[:-1])))
            y.append(int(row[-1]))
    f.close()
    return (x, y)


def info_gain(p, n):
    if not (p and n):
        return 0
    elif (p == n):
        return 1
    else:
        return ((-1 * p) / (p + n) * (math.log2(p / (p + n))) + (-1 * n) / (p + n) * (math.log2(n / (p + n))))


def entropy_attr(P, N, inf_gains, op_total):
    return ((P[0] + N[0]) * inf_gains[0] + (P[1] + N[1]) * inf_gains[1]) / (op_total)


def get_root(cols, outputs):
    if (cols == None or outputs == None):
        return
    p, n = 0, 0
    for i in outputs:
        if (i):
            p += 1
        else:
            n += 1
    mini, mini_idx = 1000, None
    for i, col in enumerate(cols):
        pair = list(zip(col, outputs))
        pos_s, neg_s = [x for x in pair if (x[0])], [x for x in pair if (not x[0])]
        P, N, inf_gains = [0, 0], [0, 0], []
        for x in pos_s:
            if (x[1]):
                P[1] += 1
            else:
                N[1] += 1
        for x in neg_s:
            if (x[1]):
                P[0] += 1
            else:
                N[0] += 1

        inf_gains.append(info_gain(P[0], N[0]))
        inf_gains.append(info_gain(P[1], N[1]))
        attr_ent = entropy_attr(P, N, inf_gains, len(outputs))
        if (attr_ent) < mini:
            mini = attr_ent
            mini_idx = i
    return mini_idx


def check_termination(node, col, output):
    if (col == [] or output == []):
        return
    pair = list(zip(col, output))
    out_pos, out_neg = [x[1] for x in pair if (x[0])], [x[1] for x in pair if (not x[0])]
    if (all(out_pos)):
        node.right = Node(value=1, is_leaf=True)
    else:
        if (not any(out_pos)):
            node.right = Node(value=0, is_leaf=True)

        else:
            node.right = Node()

    if (all(out_neg)):
        node.left = Node(value=1, is_leaf=True)
    else:
        if (not any(out_neg)):
            node.left = Node(value=0, is_leaf=True)
            return
        else:
            node.left = Node()


def traverse(root):
    if (root != None):
        traverse(root.left)
        print(root.value)
        print(root.is_leaf)
        traverse(root.right)

def build_tree(inputs, output, root):
    cols = [[inputs[j][i] for j in range(len(inputs))] for i in range(len(inputs[0]))]
    att = get_root(cols, output)
    root.value = att
    check_termination(root, cols[att], output)
    if not (root.left.is_leaf):
        delim = root.value
        data = [inputs[i] for i in range(len(inputs)) if (inputs[i][delim] == 0)]
        ops = [output[i] for i in range(len(inputs)) if (inputs[i][delim] == 0)]
        new_data = [[data[i][j] for j in range(len(data[0])) if j != delim] for i in range(len(data))]
        build_tree(new_data, ops, root.left)
    if not (root.right.is_leaf):
        delim = root.value
        data = [inputs[i] for i in range(len(inputs)) if (inputs[i][delim] == 1)]
        ops = [output[i] for i in range(len(inputs)) if (inputs[i][delim] == 1)]
        new_data = [[data[i][j] for j in range(len(data[0])) if j != delim] for i in range(len(data))]
        build_tree(new_data, ops, root.right)


ans = []
def test_example(root, inp):
    idx = root.value
    if(inp[idx]):
        if(root.right.is_leaf):
            ans.append(root.right.value)
        else:
            inp = inp[:idx] + inp[idx+1:]
            root = root.right
            test_example(root, inp)
    else:
        if (root.left.is_leaf):
            ans.append(root.left.value)
        else:
            inp = inp[:idx] + inp[idx + 1:]
            root = root.left
            test_example(root, inp)
    return ans



if __name__ == '__main__':
    inputs, output = read_csv("data2.csv")
    root = Node()
    build_tree(inputs, output, root)
    # print("traversing")
    # traverse(root)
    # print("########")
    examples= []
    with open("test2.csv") as t:
        reader = csv.reader(t)
        for row in reader:
            examples.append(list(map(int, row)))
    t.close()
    for x in examples:
        test_example(root, x)
    ans = [str(a) for a in ans]
    print(" ".join(ans))