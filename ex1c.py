import numpy as np
import matplotlib.pyplot as plt

lambdaD = 9.66e-8
sigmaP = 954*10**(-24)
A = 191
Na = 6.022*10**23

flux = np.linspace(10**11, 10**16, 1000)

tmax = np.log(lambdaD/(sigmaP*flux))/(lambdaD - sigmaP*flux)

aDmax = (Na/A) * (sigmaP*flux*lambdaD)/(lambdaD - sigmaP*flux) * (np.exp(-sigmaP*flux*tmax) - np.exp(-lambdaD*tmax))
aDth = Na * lambdaD / A  

aDmax_Ci = aDmax / (3.7e10)
aDth_Ci = aDth / (3.7e10)

plt.figure()

plt.plot(flux, aDmax_Ci, label="a_D max")
plt.plot(flux, np.full_like(flux, aDth_Ci), '--', label="a_D theory")

plt.xscale('log')
plt.yscale('log')

plt.xlabel(r"$flux\ [cm^{-2}\ s^{-1}]$")
plt.ylabel(r"$a_D$")
plt.title(r"$Maximum\ specific\ activity$")
plt.grid(which="both", linestyle="--", linewidth=0.5)
plt.legend()

plt.savefig("1b.png", dpi=300)
plt.show()

print(aDth_Ci)