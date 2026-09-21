import matplotlib.pyplot as plt

def read_xvg(filename):
    """Reads GROMACS .xvg RMSF file and returns residue and RMSF."""
    residues, rmsf_values = [], []
    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(('#', '@')) or not line.strip():
                continue
            parts = line.split()
            residues.append(float(parts[0]))
            rmsf_values.append(float(parts[1]))
    return residues, rmsf_values

# === Load RMSF data ===
residue, rmsf = read_xvg("rmsf.xvg")

# === Plot ===
plt.figure(figsize=(14, 5.2))
plt.plot(residue, rmsf, color='blue', linewidth=2.4, label='Mut_Asn')

plt.title("Root Mean Square Fluctuation (RMSF) per Residue", fontsize=14, fontweight='bold')
plt.xlabel("Residue Number", fontsize=12)
plt.ylabel("RMSF (nm)", fontsize=12)
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
plt.savefig("RMSF_blue.png", dpi=300, bbox_inches='tight')
plt.savefig("RMSF_blue.pdf", dpi=300, bbox_inches='tight')

plt.show()
