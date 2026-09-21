import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import griddata

# 1. Load the data
data = pd.read_csv('clean_fel.txt', sep='\t', header=None)
x, y, z = data[0].values, data[1].values, data[2].values

# 2. Map ASCII values to a typical kJ/mol range (Optional)
# If z is still ASCII (32-120), this shifts it to look like real Energy
z_energy = (z - np.min(z)) * 1.5 

# 3. Create a smooth grid
xi = np.linspace(x.min(), x.max(), 100)
yi = np.linspace(y.min(), y.max(), 100)
X, Y = np.meshgrid(xi, yi)
Z = griddata((x, y), z_energy, (X, Y), method='cubic')

# 4. Plotting
fig = plt.figure(figsize=(12, 9))
ax = fig.add_subplot(111, projection='3d')

# Surface plot
surf = ax.plot_surface(X, Y, Z, cmap='jet', edgecolor='none', alpha=0.9, antialiased=True)

# Add the 2D contour "shadow" on the floor (like your image)
cset = ax.contourf(X, Y, Z, zdir='z', offset=np.nanmin(Z)-5, cmap='jet', alpha=0.5)

# Labels
ax.set_xlabel('PC1')
ax.set_ylabel('PC2')
ax.set_zlabel('Free Energy (kJ/mol)')
ax.set_title('3D Free Energy Landscape')
fig.colorbar(surf, shrink=0.5, aspect=10)

plt.savefig('FEL_3D_Plot.png', dpi=300)
print("3D Funnel Plot saved as FEL_3D_Plot.png")
