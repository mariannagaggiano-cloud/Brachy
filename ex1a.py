import numpy as np
import matplotlib.pyplot as plt

lambdaD = 0.181
t = np.linspace(0, 50)
y = 1 - np.exp(-lambdaD * t)

plt.figure()
plt.plot(t, y)
plt.xlabel("days")
plt.ylabel(r"$A_D(t) / A_P(t)$")
plt.title(r"$^{222}\mathrm{Rn}$ relative activity")
plt.grid()

plt.savefig("1a.png", dpi=300)
plt.show()