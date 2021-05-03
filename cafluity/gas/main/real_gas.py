from .base_zfactor import pseudo_critical, pseudo_reduced
from .convertion import temp_FR
from .newton_rapson import newton_rapson

from .zcorrelation_azizi_behbahani_isazadeh import abi_z_factor
from .zcorrelation_brill_begg import bb_z_factor
from .zcorrelation_drancuk_abouKassem import da_func_y, da_dev_func_y, da_z_factor
from .zcorrelation_hall_yarborough import hy_func_y, hy_dev_func_y, hy_z_factor
from .zcorrelation_heidaryan_moghdasi_rahimi import hmr_z_factor
from .zcorrelation_sanjari_nemati import sn_z_factor
from .zcorrelation_new_explicit import ne_z_factor


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
		y = newton_rapson(e_tol, x0, Tpr, ppr, da_func_y, da_dev_func_y)
		z = da_z_factor(y, Tpr, ppr)

	elif zcorrelation == "hy":
		# Hall & Yarborough
		e_tol = 0.00000001
		x0 = 0
		y = newton_rapson(e_tol, x0, Tpr, ppr, hy_func_y, hy_dev_func_y)
		z = hy_z_factor(y, Tpr, ppr)

	elif zcorrelation == "abi":
		# Azizi, Behbahani, & Isazadeh
		z = abi_z_factor(Tpr, ppr)

	elif zcorrelation == "bb":
		# Brill & Begg
		z = bb_z_factor(Tpr, ppr)

	elif zcorrelation == "hmr":
		# Heidaryan, Moghdasi, & Rahimi
		z = hmr_z_factor(Tpr, ppr)

	elif zcorrelation == "sn":
		# Sanjiri & Nemati
		z = sn_z_factor(Tpr, ppr)

	elif zcorrelation == "ne":
		# New Explicit
		z = ne_z_factor(Tpr, ppr)

	return z