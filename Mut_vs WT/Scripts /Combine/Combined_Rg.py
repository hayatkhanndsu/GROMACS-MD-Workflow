import matplotlib.pyplot as plt

def read_xvg(filename):
    times, rg_values = [], []
    with open(filename, "r") as f:
        for line in f:
            if line.startswith(("#","@")) or not line.strip():
                continue
            parts = line.split()

            time_ps = float(parts[0])
            time_ns = time_ps * 0.001

            times.append(time_ns)
            rg_values.append(float(parts[1]))  # total Rg

    return times, rg_values

# Load Mut_Asn and WT_Asp
t_mut, rg_mut = read_xvg("Mut_Asn_gyrate.xvg")
t_wt, rg_wt = read_xvg("WT_Asp_gyrate.xvg")

# Plot
plt.figure(figsize=(14, 5.2))
plt.plot(t_mut, rg_mut, color='blue', linewidth=2.4, label='Mut_Asn')
plt.plot(t_wt, rg_wt, color='black', linewidth=2.4, label='WT_Asp')

plt.title("Combined Radius of Gyration (Rg) vs Time", fontsize=14, fontweight='bold')
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("Rg (nm)", fontsize=12)
plt.legend(frameon=False, fontsize=11)

plt.xlim(-2, 102)  # correct, simulation is ~10 ns (NOT 100 ns)

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

plt.savefig("Combined_Rg.png", dpi=300, bbox_inches='tight')
plt.savefig("Combined_Rg.pdf", dpi=300, bbox_inches='tight')

plt.show()
