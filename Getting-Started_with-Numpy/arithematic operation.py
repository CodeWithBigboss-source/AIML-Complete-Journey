import numpy as np
# addition
var = np.array([1,2,3,4])
varadd = var +5
print(f"addition",varadd)

# addition of arrays
var = np.array([1,2,3,4])
varr = np.array([1,2,3,4])
varradd = var + varr
print(f"addition",varradd)

# addition of 2D arrays
var = np.array([[1,2,3,4],[5,6,7,8]])
varr = np.array([[1,2,3,4],[5,6,7,8]])
# varradd = var + varr
varradd = np.add(var,varr)
print(f"addition of 2d arrays",varradd)

# subtraction
var = np.array([1,2,3,4])
varminus = var - 5
print(f"subtratcion",varminus)

# multiplication
var = np.array([1,2,3,4])
varmul = var * 5
print(f"multiplication",varmul)

# divide
var = np.array([1,2,3,4])
vardiv = var / 5
print(f"division",vardiv)

# power
var = np.array([1,2,3,4])
varpow = var ** 5
print(f"power", varpow)

# modulus
var = np.array([1,2,3,4])
varmod = var % 5
print(f"modulus", varmod)