# elementName = {ID, "name", "short name (4 characters, uppercase)", 
# description,(0 = powder, 1 = solid, 2 = liquid, 3 = energy, 4 = liquid), 
# mass, conductive (1-yes, 0-no), 
#spawnTemperature (Kelvin), meltingTemp, vaporTemp, menuColor, elementColor}

from ursina import *

# Iron
elementIron = [1, "Iron", "IRON", "the average material, still doesnt rust tho", 1, 2, 1, 298, 1773, (2861 + 273), color.rgb(203, 205, 205), color.rgb(203, 205, 205)]