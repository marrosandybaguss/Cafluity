from .base_zfactor import pseudo_critical, pseudo_reduced
from .convertion import temp_FR
from .newton_rapson import newton_rapson

from . import zcorrelation_azizi_behbahani_isazadeh as abi
from . import zcorrelation_brill_begg as bb
from . import zcorrelation_drancuk_abouKassem as da
from . import zcorrelation_hall_yarborough as hy
from . import zcorrelation_heidaryan_moghdasi_rahimi as hmr
from . import zcorrelation_sanjari_nemati as sn
from . import zcorrelation_new_explicit as ne


R = 10.730 #  psia ft3/lb-mole °R
Mair = 28.96 # lb / lb-mol

# apparent molecular weight
def Ma(Yg = 1, Mair = Mair):
	return Mair*Yg

# specific gravity
def Yg(Ma = 1, Mair = Mair):
	return Ma/Mair

# density
def rho_g(p = 1, T = 1, Ma = 1, z = 1):
	return round((p*Ma/(z*R*T)),4)

# specific volume
def v(p = 1, T = 1, Ma = 1, z = 1):
	return round((z*R*T/(p*Ma)),4)

# z gas factor
def z(Tpr, ppr, zcorrelation = "da-k"):
	
	if zcorrelation == "da-k":
		name = "Drancuk & Abou-Kassem's Z Factor Correlation"
		e_tol = 0.00000001
		x0 = 0.3
		y = newton_rapson(e_tol, x0, Tpr, ppr, da.func_y, da.dev_func_y)
		z = da.z_factor(y, Tpr, ppr)
		boundary = {
			"minTpr": da.minTpr, 
			"maxTpr": da.maxTpr, 
			"minPpr": da.minPpr, 
			"maxPpr": da.maxPpr
			}

	elif zcorrelation == "hy":
		name = "Hall & Yarborough's Z Factor Correlation"
		e_tol = 0.00000001
		x0 = 0
		y = newton_rapson(e_tol, x0, Tpr, ppr, hy.func_y, hy.dev_func_y)
		z = hy.z_factor(y, Tpr, ppr)
		boundary = {
			"minTpr": hy.minTpr, 
			"maxTpr": hy.maxTpr, 
			"minPpr": hy.minPpr, 
			"maxPpr": hy.maxPpr
			}

	elif zcorrelation == "abi":
		name = "Azizi, Behbahani, & Isazadeh's Z Factor Correlation"
		z = abi.z_factor(Tpr, ppr)
		boundary = {
			"minTpr": abi.minTpr, 
			"maxTpr": abi.maxTpr, 
			"minPpr": abi.minPpr, 
			"maxPpr": abi.maxPpr
			}

	elif zcorrelation == "bb":
		name = "Brill & Begg's Z Factor Correlation"
		z = bb.z_factor(Tpr, ppr)
		boundary = {
			"minTpr": bb.minTpr, 
			"maxTpr": bb.maxTpr, 
			"minPpr": bb.minPpr, 
			"maxPpr": bb.maxPpr
			}

	elif zcorrelation == "hmr":
		name = "Heidaryan, Moghdasi, & Rahimi's Z Factor Correlation"
		z = hmr.z_factor(Tpr, ppr)
		boundary = {
			"minTpr": hmr.minTpr, 
			"maxTpr": hmr.maxTpr, 
			"minPpr": hmr.minPpr, 
			"maxPpr": hmr.maxPpr,
			"noPpr": hmr.noPpr
			}

	elif zcorrelation == "sn":
		name = "Sanjiri & Nemati's Z Factor Correlation"
		z = sn.z_factor(Tpr, ppr)
		boundary = {
			"minTpr": sn.minTpr, 
			"maxTpr": sn.maxTpr, 
			"minPpr": sn.minPpr, 
			"maxPpr": sn.maxPpr,
			"noPpr": sn.noPpr
			}

	elif zcorrelation == "ne":
		name = "New Explicit Z Factor Correlation"
		z = ne.z_factor(Tpr, ppr)
		boundary = {
			"minTpr": ne.minTpr, 
			"maxTpr": ne.maxTpr, 
			"minPpr": ne.minPpr, 
			"maxPpr": ne.maxPpr
			}

	return name, boundary, z

def z_graph(Tpr, ppr, zcorrelation = "da-k"):
	if zcorrelation == "da-k":
		# Drancuk & Abou-Kassem
		e_tol = 0.00000001
		x0 = 0.3
		zGraph = da.graph(Tpr, ppr, e_tol, x0)

	elif zcorrelation == "hy":
		# Hall & Yarborough
		e_tol = 0.00000001
		x0 = 0
		zGraph = hy.graph(Tpr, ppr, e_tol, x0)

	elif zcorrelation == "abi":
		# Azizi, Behbahani, & Isazadeh
		zGraph = abi.graph(Tpr, ppr)

	elif zcorrelation == "bb":
		# Brill & Begg
		zGraph = bb.graph(Tpr, ppr)

	elif zcorrelation == "hmr":
		# Heidaryan, Moghdasi, & Rahimi
		zGraph = hmr.graph(Tpr, ppr)

	elif zcorrelation == "sn":
		# Sanjiri & Nemati
		zGraph = sn.graph(Tpr, ppr)

	elif zcorrelation == "ne":
		# New Explicit
		zGraph = ne.graph(Tpr, ppr)

	return zGraph

