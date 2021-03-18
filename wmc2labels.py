import scipy.io as sio
import numpy as np
import json
import csv

if __name__ == '__main__':

	with open('config.json') as f:
		config = json.load(f)
		fname = config["classification"]
		tractID_list = config["tractID_list"]

	wmc = sio.loadmat(fname)
	data = wmc['classification'][0][0]
	index = data['index']
	names = data['names'][0]

	if tractID_list != "all":
		print("Keeping only some of the tracts")
		tractID_list = np.array(eval(tractID_list), ndmin=1)
		for i, ind in enumerate(index):
			if ind not in tractID_list:
				index[i] = 0
		for n, name in enumerate(names):
			if n+1 not in tractID_list:
				names[n][0] = 'NC'

	index_structure = 'index.csv'
	print('Writing indeces in ' + index_structure)
	for ind in index:
		with open(index_structure, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow([int(ind)])

	names_structure = 'names.csv'
	print('Writing names in ' + names_structure)
	for n in range(len(names)):
		if n==0:
			row = [0, 'NC']
		else:
			name = names[n-1][0]
			row = [n, name.replace(" ", "_")]
		print(row)
		with open(names_structure, 'a') as csvFile:
			writer = csv.writer(csvFile)
			writer.writerow(row)		

