import matplotlib.pyplot as plt

def read_xvg(filename):
    """Reads GROMACS .xvg SASA file and returns time in ns and SASA in nm^2."""
    times, sasa_values = [], []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(('#', '@')) or not line.strip():
                continue
            parts = line.split()

            # Convert ps → ns
            times.append(float(parts[0]) * 0.001)

            sasa_values.append(float(parts[1]))
    return times, sasa_values

# === Load SASA data ===
time, sasa = read_xvg("sasa_total.xvg")

# === Plot ===
plt.figure(figsize=(14, 5.2))
plt.plot(time, sasa, color='blue', linewidth=2.4, label='Mut_Asn')

plt.title("Solvent Accessible Surface Area (SASA) vs Time", fontsize=14, fontweight='bold')
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("SASA (nm²)", fontsize=12)
plt.legend(frameon=False, fontsize=11)

# Frame & border styling
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.2)
    spine.set_color('black')

# Add spacing on both left and right
plt.xlim(-2, 102)
plt.margins(x=0.03)

# Clean layout with extra padding
plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.98])

# Save
plt.savefig("SASA_blue.png", dpi=300, bbox_inches='tight')
plt.savefig("SASA_blue.pdf", dpi=300, bbox_inches='tight')

plt.show()
