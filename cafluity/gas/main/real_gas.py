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
def rho_g(p = 1, T = 1, Yg = 1, z = 1):
	return p*Ma(Yg)/(z*R*T)

# specific volume
def v(rho_g = 1):
	return 1/rho_g

def v(p = 1, T = 1, Ma = 1, z = 1):
	return z*R*T/(p*Ma)

# z gas factor
def z(Tpr, ppr, zcorrelation = "da-k"):

	if zcorrelation == "da-k":
		# Drancuk & Abou-Kassem
		e_tol = 0.00000001
		x0 = 0.3
		y = newton_rapson(e_tol, x0, Tpr, ppr, da.func_y, da.dev_func_y)
		z = da.z_factor(y, Tpr, ppr)

	elif zcorrelation == "hy":
		# Hall & Yarborough
		e_tol = 0.00000001
		x0 = 0
		y = newton_rapson(e_tol, x0, Tpr, ppr, hy.func_y, hy.dev_func_y)
		z = hy.z_factor(y, Tpr, ppr)

	elif zcorrelation == "abi":
		# Azizi, Behbahani, & Isazadeh
		z = abi.z_factor(Tpr, ppr)

	elif zcorrelation == "bb":
		# Brill & Begg
		z = bb.z_factor(Tpr, ppr)

	elif zcorrelation == "hmr":
		# Heidaryan, Moghdasi, & Rahimi
		z = hmr.z_factor(Tpr, ppr)

	elif zcorrelation == "sn":
		# Sanjiri & Nemati
		z = sn.z_factor(Tpr, ppr)

	elif zcorrelation == "ne":
		# New Explicit
		z = ne.z_factor(Tpr, ppr)

	return z

def z_graph(Tpr, ppr, zcorrelation = "da-k"):
	if zcorrelation == "da-k":
		# Drancuk & Abou-Kassem
		e_tol = 0.00000001
		x0 = 0.3
		y = newton_rapson(e_tol, x0, Tpr, ppr, da_func_y, da_dev_func_y)
		zGraph = da_z_factor(y, Tpr, ppr)

	elif zcorrelation == "hy":
		# Hall & Yarborough
		e_tol = 0.00000001
		x0 = 0
		y = newton_rapson(e_tol, x0, Tpr, ppr, hy_func_y, hy_dev_func_y)
		zGraph = hy_z_factor(y, Tpr, ppr)

	elif zcorrelation == "abi":
		# Azizi, Behbahani, & Isazadeh
		zGraph = abi_z_factor(Tpr, ppr)

	elif zcorrelation == "bb":
		# Brill & Begg
		zGraph = bb_z_factor(Tpr, ppr)

	elif zcorrelation == "hmr":
		# Heidaryan, Moghdasi, & Rahimi
		zGraph = hmr_z_factor(Tpr, ppr)

	elif zcorrelation == "sn":
		# Sanjiri & Nemati
		zGraph = sn_z_factor(Tpr, ppr)

	elif zcorrelation == "ne":
		# New Explicit
		zGraph = ne.graph(Tpr, ppr)

	return zGraph