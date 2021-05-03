def brown(gasGravity = 1, co2 = 0, h2s = 0, n2 = 0):
  # Natural Gas Systems
  Tpc = 168 + 325*gasGravity - 12.5*gasGravity**2
  ppc = 677 + 15*gasGravity - 37.5*gasGravity**2
  # With effect nonhydrocarbon components
  # The Carr-Kobayashi-Burrows Correction Method
  Tpc = round((Tpc - 80*co2/100 + 130*h2s/100 - 250*n2/100),4)
  ppc = round((ppc + 440*co2/100 + 600*h2s/100 - 170*n2/100),4)

  return Tpc, ppc

def sutton(gasGravity = 1, co2 = 0, h2s = 0, n2 = 0):
  # Without effect nonhydrocarbon components
  # Sutton Correlation
  Tpc = 169.2 + 349.5*gasGravity - 74*gasGravity**2
  ppc = 756.8 - 131.07*gasGravity - 3.6*gasGravity**2
  # With effect nonhydrocarbon components
  # The Carr-Kobayashi-Burrows Correction Method
  Tpc = round((Tpc - 80*co2/100 + 130*h2s/100 - 250*n2/100),4)
  ppc = round((ppc + 440*co2/100 + 600*h2s/100 - 170*n2/100),4)

  return Tpc, ppc

