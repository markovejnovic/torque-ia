#!/usr/bin/env python

import matplotlib.pyplot as plt

import csv

x = []
y = []

with open('data.csv', 'r') as f:
	reader = csv.reader(f)
	for row in reader:
		x.append(float(row[0]))
		y.append(float(row[1]))

plt.plot(x, y, 'r.')
plt.show()