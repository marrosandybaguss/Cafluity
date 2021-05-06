"""
cannot be used to evaluate the derivative of the zfactor 
with respect to the pseudo-reduced pressure at Ppr = 3

This correlation, however, is less efficient when
compared with that of Heidaryan et al.

Therefore, the actual maximum error for
this correlation is 104.3206 %.
"""

import math
import matplotlib.pyplot as plt
from .graph import get_plot

maxTpr = 3
minTpr = 1.15
maxPpr = 15
minPpr = 0.2
noPpr = 3

def boundary_check(Tpr, Ppr):
	if Tpr < minTpr or Tpr > maxTpr:
		return 0
	
	if Ppr < minPpr or Ppr > maxPpr:
		return 0

	if Ppr == noPpr:
		return 0

	return 1

def constants(Ppr = 1):
	if Ppr <= 3:
		A1 = 0.007698
		A2 = 0.003839
		A3 = -0.467212
		A4 = 1.018801
		A5 = 3.805723
		A6 = -0.087361
		A7 = 7.138305
		A8 = 0.083440
	else:
		A1 = 0.015642
		A2 = 0.000701
		A3 = 2.341511
		A4 = -0.657903
		A5 = 8.902112
		A6 = -1.136000
		A7 = 3.543614
		A8 = 0.134041
	return A1, A2, A3, A4, A5, A6, A7, A8

def z_factor(Tpr = 1, Ppr = 1):
	if boundary_check(Tpr, Ppr):
		A1, A2, A3, A4, A5, A6, A7, A8 = constants(Ppr)
		z = 1 + A1*Ppr + A2*Ppr**2 + (A3*Ppr**A4)/Tpr**A5 + (A6*Ppr**(A4 + 1))/Tpr**A7 + (A8*Ppr**(A4 + 2))/Tpr**(A7 + 1)
		return round(z,4)
	else:
		return "NULL"

def multi_graph(Tpr = 1, Ppr = 1):
	
	tpr = Tpr - 0.45
	tpri = []
	for i in range(0,18):
		tpri.append(tpr)
		tpr = tpr + 0.05

	x = []
	y = []
	for i in range(0,18):
		y.append([])

	ppr = Ppr - 2
	for i in range(1,120):
		x.append(ppr)

		for i in range(0,18):
			z = z_factor(tpri[i], ppr)
			y[i].append(z)

		ppr = ppr + 0.1
	  
	# plotting the points  
	for i in range(0,18):
		plt.plot(x, y[i])

	plt.legend(["Tpr = " + str(tpri[0]), "Tpr = " + str(tpri[1]), "Tpr = " + str(tpri[2]), "Tpr = " + str(tpri[3]), "Tpr = " + str(tpri[4]), "Tpr = " + str(tpri[5]), "Tpr = " + str(tpri[6]),  "Tpr = " + str(tpri[7]), "Tpr = " + str(tpri[8]), "Tpr = " + str(tpri[9]), "Tpr = " + str(tpri[10]), "Tpr = " + str(tpri[11]), "Tpr = " + str(tpri[12]),  "Tpr = " + str(tpri[13]), "Tpr = " + str(tpri[14]),"Tpr = " + str(tpri[15]), "Tpr = " + str(tpri[16]),  "Tpr = " + str(tpri[17])], loc='upper right', bbox_to_anchor=(1.3, 0.5, 0.5, 0.5))
	
	# naming the x axis 
	plt.xlabel('Pseudoreduced Pressure Ppr') 
	# naming the y axis 
	plt.ylabel('Compressibility Factor z') 
	  
	# giving a title to my graph 
	plt.title("Sanjari & Nemati's Correlation") 
	  
	# function to show the plot 
	plt.show()

def graph(Tpr = 1, Ppr = 1):
	ppr = Ppr - 1.5
	x = []
	y = []

	for i in range(1,30):
		ppr = ppr + 0.1
		z = z_factor(Tpr, ppr)
		x.append(ppr)
		y.append(z)

	title = "Sanjari's Correlation"
	xlabel = 'Pseudoreduced Pressure Ppr'
	ylabel = 'Compressibility Factor z'

	chart = get_plot(x, y, title, xlabel, ylabel)

	return chart
