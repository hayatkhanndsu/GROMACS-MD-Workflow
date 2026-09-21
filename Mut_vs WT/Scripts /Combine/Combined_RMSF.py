import matplotlib.pyplot as plt

def read_xvg(filename):
    residues, rmsf_values = [], []
    with open(filename, "r") as f:
        for line in f:
            if line.startswith(("#","@")) or not line.strip():
                continue
            parts = line.split()
            residues.append(int(float(parts[0])))   # residue index
            rmsf_values.append(float(parts[1]))     # RMSF value
    return residues, rmsf_values

# === Load Mut_Asn RMSF ===
res_mut, rmsf_mut = read_xvg("Mut_Asn_rmsf.xvg")

# === Load WT_Asp RMSF ===
res_wt, rmsf_wt = read_xvg("WT_Asp_rmsf.xvg")

# === Plot ===
plt.figure(figsize=(14, 5.2))

# Mut_Asn (blue)
plt.plot(res_mut, rmsf_mut, color='blue', linewidth=2.4, label='Mut_Asn')

# WT_Asp (black)
plt.plot(res_wt, rmsf_wt, color='black', linewidth=2.4, label='WT_Asp')

plt.title("Combined RMSF per Residue", fontsize=14, fontweight='bold')
plt.xlabel("Residue Number", fontsize=12)
plt.ylabel("RMSF (nm)", fontsize=12)
plt.legend(frameon=False, fontsize=11)

# Frame styling
ax = plt.gca()
for spine in ax.spines.values():
    spine.set_visible(True)
    spine.set_linewidth(1.2)
    spine.set_color('black')

plt.margins(x=0.02, y=0.05)
plt.tick_params(direction='out', length=4, width=1, colors='black')
plt.grid(False)
plt.tight_layout()

plt.savefig("Combined_RMSF.png", dpi=300, bbox_inches='tight')
plt.savefig("Combined_RMSF.pdf", dpi=300, bbox_inches='tight')

plt.show()
