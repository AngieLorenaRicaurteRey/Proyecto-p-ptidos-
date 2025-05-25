import matplotlib.pyplot as plt
import numpy as np

#De 16 a 1mM hasta 0
P_L = np.array([0.32,0.2,0.16,0.12,0.08,0.04,0])
GP_raw = np.array([0.503971035,0.514783085,0.509682383,0.510495148,0.50265595,0.494934015,0.439834679])
desviaciones = np.array([0.016255043,0.004655778,0.006183317,0.002092531,0.001472319,0.004429647,0.011404009])

colors = plt.cm.viridis(np.linspace(0, 1, len(P_L)))

fig, ax = plt.subplots()

for i in range(len(GP_raw)):
    ax.errorbar(P_L[i], GP_raw[i],
                yerr=desviaciones[i],
                fmt='o', color=colors[i], label=f'{P_L[i]} ',
                capsize=5)

ax.set_xlabel('P/L')
ax.set_ylabel('GPolarización')
ax.set_title('Efecto de PIAM 21-7 sobre membrana de S.Aureus a 21°C')

ax.legend(title='P/L')

plt.xlim(-0.01, 0.23)

plt.grid(True)
plt.tight_layout()
plt.show()

