import matplotlib.pyplot as plt

def read_xvg(filename, scale_time=1):
    """Reads GROMACS .xvg RMSD file and returns time (ns) and RMSD (nm)."""
    times, rmsd_values = [], []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(('#', '@')) or not line.strip():
                continue
            parts = line.split()
            times.append(float(parts[0]) * 0.001)   # convert ps → ns
            rmsd_values.append(float(parts[1]))
    return times, rmsd_values

# === Load RMSD data ===
time, rmsd = read_xvg("rmsd.xvg", scale_time=1)

# === Plot ===
plt.figure(figsize=(14, 5.2))
plt.plot(time, rmsd, color='blue', linewidth=2.4, label='Mut_Asn')

plt.title("Root Mean Square Deviation (RMSD) vs Time", fontsize=14, fontweight='bold')
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("RMSD (nm)", fontsize=12)
plt.legend(frameon=False, fontsize=11)

# Frame & border styling
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.2)
    spine.set_color('black')

plt.margins(x=0.02, y=0.05)
plt.tick_params(direction='out', length=4, width=1, colors='black')
plt.grid(False)
plt.tight_layout()

# Save
plt.savefig("RMSD_blue.png", dpi=300, bbox_inches='tight')
plt.savefig("RMSD_blue.pdf", dpi=300, bbox_inches='tight')

plt.show()
