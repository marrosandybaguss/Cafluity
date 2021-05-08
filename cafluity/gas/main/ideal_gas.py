R = 10.730 #  psia ft3/lb-mole °R
Mair = 28.96 # lb / lb-mol

def Ma(Yg = 1, Mair = Mair):
	return round((Mair*Yg),4)

def rho_g(p = 1, Ma = 1, T = 1):
	return round((p*Ma/(R*T)),4)

def v(rho_g = 1):
	return 1/rho_g

def v(p = 1, Ma = 1, T = 1):
	return round((R*T/(p*Ma)),4)

def Yg(Ma = 1, Mair = Mair):
	return round((Ma/Mair),4)

