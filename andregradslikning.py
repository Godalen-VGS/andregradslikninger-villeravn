import math

def losninger(a, b, c):
  #skjekk antall losninger
  diskriminant = b**2 - 4*a*c
  
  #returner riktige antall verdier basert på diskriminanten
  if diskriminant < 0:
    return "Ingen losninger"
  
  losning1 = (-b - math.sqrt(diskriminant)) / (2*a)
  round(losning1,2)
  
  losning2 = (-b + math.sqrt(diskriminant)) / (2*a)
  round(losning2,2)

  if diskriminant == 0:

    return losning1
  
  elif diskriminant > 0:
    return (losning1, losning2)