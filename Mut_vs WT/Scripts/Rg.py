import matplotlib.pyplot as plt

def read_xvg(filename):
    """Reads GROMACS .xvg file and returns time in ns and Rg in nm."""
    times, rg_values = [], []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(('#', '@')) or not line.strip():
                continue
            parts = line.split()

            # Convert ps → ns (GROMACS default for time)
            times.append(float(parts[0]) * 0.001)

            rg_values.append(float(parts[1]))
    return times, rg_values

# === Load Rg data ===
time, rg = read_xvg("gyrate.xvg")

# === Plot ===
plt.figure(figsize=(14, 5.2))
plt.plot(time, rg, color='blue', linewidth=2.4, label='Mut_Asn')

plt.title("Radius of Gyration (Rg) vs Time", fontsize=14, fontweight='bold')
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("Rg (nm)", fontsize=12)
plt.legend(frameon=False, fontsize=11)

# Frame & border styling
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.2)
    spine.set_color('black')

plt.margins(x=0.6, y=0.05)
plt.tick_params(direction='out', length=4, width=1, colors='black')
plt.grid(False)

plt.xlim(-2, 102)  # Show full 0–100 ns range
plt.tight_layout(rect=[0.02, 0.02, 0.98, 0.98])

# Save
plt.savefig("Rg_blue.png", dpi=300, bbox_inches='tight')
plt.savefig("Rg_blue.pdf", dpi=300, bbox_inches='tight')

plt.show()
