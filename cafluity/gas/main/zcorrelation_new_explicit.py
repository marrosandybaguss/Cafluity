# A new explicit z-factor is developed as a multi-stage correlation 
# based on Hall and Yarborough’s implicit correlation.

# The y-values on the right side of the expression were replaced by
# Non-linear regression was performed using the derived model

import math
import matplotlib.pyplot as plt

a1 = 0.317842
a2 = 0.382216
a3 = -7.768354
a4 = 14.290531
a5 = 0.000002
a6 = -0.004693
a7 = 0.096254
a8 = 0.166720
a9 = 0.966910
a10 = 0.063069
a11 = -1.966847
a12 = 21.0581
a13 = -27.0246
a14 = 16.23
a15 = 207.783
a16 = -488.161
a17 = 176.29
a18 = 1.88453
a19 = 3.05921

def t(Tpr = 1):
	return 1/Tpr

def A(Tpr = 1, Ppr = 1):
	return a1*t(Tpr)*Ppr*math.e**(a2*(1-t(Tpr))**2)

def B(Tpr = 1, Ppr = 1):
	return a3*t(Tpr) + a4*t(Tpr)**2 + a5*(t(Tpr)**6)*(Ppr**6)

def C(Tpr = 1, Ppr = 1):
	return a9 + a8*t(Tpr)*Ppr + a7*(t(Tpr)**2)*(Ppr**2) + a6*(t(Tpr)**3)*(Ppr**3)

def D(Tpr = 1):
	return a10*t(Tpr)*math.e**(a11*(1-t(Tpr))**2)

def E(Tpr = 1):
	return a12*t(Tpr) + a13*t(Tpr)**2 + a14*t(Tpr)**3

def F(Tpr = 1):
	return a15*t(Tpr) + a16*t(Tpr)**2 + a17*t(Tpr)**3

def G(Tpr = 1):
	return a18 + a19*t(Tpr)

def y(Tpr = 1, Ppr = 1):
	upper = D(Tpr)*Ppr
	left = (1 + A(Tpr, Ppr)**2)/C(Tpr, Ppr)
	right = (B(Tpr, Ppr)*A(Tpr, Ppr)**2)/C(Tpr, Ppr)**3

	return upper / (left - right)

def ne_z_factor(Tpr = 1, Ppr = 1):
	upper = D(Tpr)*Ppr*(1 + y(Tpr, Ppr) + y(Tpr, Ppr)**2 - y(Tpr, Ppr)**3)
	lower = (D(Tpr)*Ppr + E(Tpr)*y(Tpr, Ppr)**2 - F(Tpr)*y(Tpr, Ppr)**G(Tpr))*((1 - y(Tpr, Ppr))**3)

	return round((upper/lower),4)

def multi_graph(Tpr = 1, Ppr = 1):
	
	tpr1 = Tpr - 0.45
	tpr2 = Tpr - 0.40
	tpr3 = Tpr - 0.35
	tpr4 = Tpr - 0.30
	tpr5 = Tpr - 0.25
	tpr6 = Tpr - 0.20
	tpr7 = Tpr - 0.15
	tpr8 = Tpr - 0.10
	tpr9 = Tpr - 0.05
	tpr10 = Tpr
	tpr11 = Tpr + 0.05
	tpr12 = Tpr + 0.10
	tpr13 = Tpr + 0.15
	tpr14 = Tpr + 0.20
	tpr15 = Tpr + 0.25
	tpr16 = Tpr + 0.30
	tpr17 = Tpr + 0.35
	tpr18 = Tpr + 0.40

	x = []
	y1 = []
	y2 = []
	y3 = []
	y4 = []
	y5 = []
	y6 = []
	y7 = []
	y8 = []
	y9 = []
	y10 = []
	y11 = []
	y12 = []
	y13 = []
	y14 = []
	y15 = []
	y16 = []
	y17 = []
	y18 = []

	ppr = Ppr - 2
	for i in range(1,120):
		x.append(ppr)

		z1 = z_factor(tpr1, ppr)
		y1.append(z1)
		z2 = z_factor(tpr2, ppr)
		y2.append(z2)
		z3 = z_factor(tpr3, ppr)
		y3.append(z3)
		z4 = z_factor(tpr4, ppr)
		y4.append(z4)
		z5 = z_factor(tpr5, ppr)
		y5.append(z5)
		z6 = z_factor(tpr6, ppr)
		y6.append(z6)
		z7 = z_factor(tpr7, ppr)
		y7.append(z7)
		z8 = z_factor(tpr8, ppr)
		y8.append(z8)
		z9 = z_factor(tpr9, ppr)
		y9.append(z9)
		z10 = z_factor(tpr10, ppr)
		y10.append(z10)
		z11 = z_factor(tpr11, ppr)
		y11.append(z11)
		z12 = z_factor(tpr12, ppr)
		y12.append(z12)
		z13 = z_factor(tpr13, ppr)
		y13.append(z13)
		z14 = z_factor(tpr14, ppr)
		y14.append(z14)
		z15 = z_factor(tpr15, ppr)
		y15.append(z15)
		z16 = z_factor(tpr16, ppr)
		y16.append(z16)
		z17 = z_factor(tpr17, ppr)
		y17.append(z17)
		z18 = z_factor(tpr18, ppr)
		y18.append(z18)

		ppr = ppr + 0.1
	  
	# plotting the points  
	plt.plot(x, y1)
	plt.plot(x, y2)
	plt.plot(x, y3)
	plt.plot(x, y4)
	plt.plot(x, y5)
	plt.plot(x, y6)
	plt.plot(x, y7)
	plt.plot(x, y8)
	plt.plot(x, y9)
	plt.plot(x, y10)
	plt.plot(x, y11)
	plt.plot(x, y12)
	plt.plot(x, y13)
	plt.plot(x, y14)
	plt.plot(x, y15)
	plt.plot(x, y16)
	plt.plot(x, y17)
	plt.plot(x, y18)

	plt.legend(["Tpr = " + str(tpr1), "Tpr = " + str(tpr2), "Tpr = " + str(tpr3), "Tpr = " + str(tpr4), "Tpr = " + str(tpr5), "Tpr = " + str(tpr6),  "Tpr = " + str(tpr7), "Tpr = " + str(tpr8), "Tpr = " + str(tpr9), "Tpr = " + str(tpr10), "Tpr = " + str(tpr11), "Tpr = " + str(tpr12),  "Tpr = " + str(tpr13), "Tpr = " + str(tpr14),"Tpr = " + str(tpr15), "Tpr = " + str(tpr16),  "Tpr = " + str(tpr17), "Tpr = " + str(tpr18)], loc='upper right', bbox_to_anchor=(1.3, 0.5, 0.5, 0.5))
	
	# naming the x axis 
	plt.xlabel('Pseudoreduced Pressure Ppr') 
	# naming the y axis 
	plt.ylabel('Compressibility Factor z') 
	  
	# giving a title to my graph 
	plt.title("New Explicit Correlation") 
	  
	# function to show the plot 
	plt.show()

def ne_graph(Tpr = 1, Ppr = 1):
	ppr = Ppr # ada masalah ketika dikurangi 2, keterangan erornya itu nilai upper dan lower di ne_z_factor sangat kecil mendekati nol
	z = ne_z_factor(Tpr, ppr)
	x = []
	y = []

	for i in range(1,30):
		ppr = ppr + 0.1
		z = ne_z_factor(Tpr, ppr)
		x.append(ppr)
		y.append(z)

	return x, y

	# plotting the points
	# graphPlot = plt.plot(x, y)
		
	# plt.xlabel('Pseudoreduced Pressure Ppr')
	# plt.ylabel('Compressibility Factor z')
	# plt.title("New Explicit Correlation")

	# return graphPlot
