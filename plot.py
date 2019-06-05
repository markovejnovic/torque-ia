#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import csv
import sys

t = []
rev = []
theta = []

drev_dt = []

t_avg = []
rev_avg = []
theta_avg = []

drev_avg_dt = []

v_final = 0
theta_final = 0

def read(path):
	global t
	global rev
	global theta

	with open(path, 'r') as f:
		reader = csv.reader(f)

		is_first = True
		for row in reader:
			if is_first:
				is_first = False
				continue
			t.append(float(row[0]) / 1000)
			rev.append(np.pi * 2 * float(row[1]) / 4)
			theta.append(300 / 1024 * float(row[2]))

	theta_new = []
	for v in theta:
		theta_new.append(v - theta[0])
	theta = theta_new

def calculate_avg():
	global t_avg
	global rev_avg
	global theta_avg

	i = 0
	last_rev = 0
	n = 0
	time_sum = 0
	theta_sum = 0
	while i < len(rev):
		if rev[i] == last_rev:
			time_sum += t[i]
			theta_sum += theta[i]
			n += 1
		else:
			t_avg.append(time_sum / n)
			rev_avg.append(last_rev)
			theta_avg.append(theta_sum / n)

			last_rev = rev[i]
			time_sum = t[i]
			theta_sum = theta[i]
			n = 1
		i += 1

def diff():
	global drev_dt
	global drev_avg_dt

	drev_dt = np.diff(rev) / np.diff(t)
	drev_avg_dt = np.diff(rev_avg) / np.diff(t_avg)

def plot_v_over_t():
	plt.plot(t, rev, '.')
	plt.plot(t_avg, rev_avg, '.')

	plt.plot(t_avg[0:-1], drev_avg_dt)

	plt.xlabel("Time [s]")
	plt.ylabel(u"Angular path [2 \u03C0]\n " +
		u"Derivative of angle - angular velocity [\u00B0 / s]")

def plot_theta_over_v():
	plt.plot(t_avg, theta_avg)

def plot_all():
	plt.plot(t, rev, '.', 
		label=u'Raw angular path [2 \u03C0]')
	plt.plot(t_avg, rev_avg, '.', 
		label=u'Averaged angular path [2 \u03C0]')

	plt.plot(t_avg[0:-1], drev_avg_dt, 
		label=u'Angular velocity [2 \u03C0 / s]')

	plt.plot(t_avg, theta_avg, 
		label=u'Angle of inclination [\u00B0]')

	plt.xlabel('Time [s]')

	plt.legend()

def calculate_final(plot=False):
	global v_final
	global theta_final

	v_final = np.mean(np.array(drev_avg_dt))
	theta_final = max(theta_avg) - min(theta_avg)

	if plot:
		plt.plot(v_final, 0, 'yo')

	print(str(v_final) + ',' + \
		str(theta_final) + ',' + \
		str(np.std(np.array(drev_avg_dt))) + ',' + \
		str(np.pi / 4))

if __name__ == '__main__':
	read(sys.argv[-1])
	calculate_avg()
	diff()

	calculate_final()

	plot_all()

	plt.show()