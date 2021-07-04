from .pc_correlation import brown, sutton

def pseudo_critical(gasGravity = 1, co2 = 0, h2s = 0, n2 = 0, correlation = "sutton"):
  if correlation == "sutton" :
    return sutton(gasGravity, co2, h2s, n2)
  elif correlation == "brown" :
    return brown(gasGravity, co2, h2s, n2)

def pseudo_reduced(temperature = 1, pressure = 1, Tpc = 1, Ppc = 1):
  if temperature == 0 or pressure == 0:
    Tpr = "NULL"
    ppr = "NULL"
  else:
    Tpr = round((temperature/Tpc),4)
    ppr = round((pressure/Ppc),4)

  return Tpr, ppr
