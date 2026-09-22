import matplotlib.pyplot as plt

def read_xvg(filename):
    times = []
    sasa_values = []

    with open(filename, "r") as f:
        for line in f:
            if line.startswith(("#","@")) or not line.strip():
                continue

            parts = line.split()
            t_ps = float(parts[0])           # Time in ps
            sasa = float(parts[1])           # SASA in nm^2

            # Convert ps → ns
            t_ns = t_ps / 1000.0

            times.append(t_ns)
            sasa_values.append(sasa)

    return times, sasa_values


# Load files (both in ps → convert to ns)
time_mut, sasa_mut = read_xvg("Mut_Asn_sasa.xvg")
time_wt, sasa_wt  = read_xvg("WT_Asp_sasa_total.xvg")

# === Plot ===
plt.figure(figsize=(14, 5.5))

# Blue for Mut_Asn
plt.plot(time_mut, sasa_mut, color='blue', linewidth=2.4, label='Mut_Asn')

# Black for WT_Asp
plt.plot(time_wt, sasa_wt, color='black', linewidth=2.4, label='WT_Asp')

plt.title("Combined SASA vs Time", fontsize=14, fontweight='bold')
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("SASA (nm²)", fontsize=12)
plt.legend(frameon=False, fontsize=11)

plt.xlim(-2, 102)

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

plt.savefig("Combined_SASA.png", dpi=300, bbox_inches='tight')
plt.savefig("Combined_SASA.pdf", dpi=300, bbox_inches='tight')

plt.show()
