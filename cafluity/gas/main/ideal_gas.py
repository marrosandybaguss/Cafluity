R = 10.730 #  psia ft3/lb-mole °R
Mair = 28.96 # lb / lb-mol

def Ma(Yg = 1, Mair = Mair):
	return Mair*Yg

def rho_g(p = 1, Ma = 1, T = 1):
	return p*Ma/(R*T)

def v(rho_g = 1):
	return 1/rho_g

def v(p = 1, Ma = 1, T = 1):
	return R*T/(p*Ma)

def Yg(Ma = 1, Mair = Mair):
	return Ma/Mair

