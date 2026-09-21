import matplotlib.pyplot as plt

def read_xvg(filename, convert_ps_to_ns=False):
    times = []
    values = []

    with open(filename, 'r') as f:
        for line in f:
            if line.startswith(('#', '@')) or not line.strip():
                continue

            parts = line.split()
            t = float(parts[0])
            v = float(parts[1])

            # Convert Mut_Asn time from ps → ns
            if convert_ps_to_ns:
                t = t / 1000.0

            times.append(t)
            values.append(v)

    return times, values


# Load WT_Asp (already in ns)
time_wt, rmsd_wt = read_xvg("WT_Asp_rmsd.xvg")

# Load Mut_Asn (must convert from ps → ns)
time_mut, rmsd_mut = read_xvg("Mut_Asn_rmsd.xvg", convert_ps_to_ns=True)


plt.figure(figsize=(14, 5.5))

plt.plot(time_mut, rmsd_mut, color='blue', linewidth=1.5, label="Mut_Asn")
plt.plot(time_wt, rmsd_wt, color='black', linewidth=1.0, label="WT_Asp")

plt.title("Combined RMSD vs Time", fontsize=14, fontweight='bold')
plt.xlabel("Time (ns)", fontsize=12)
plt.ylabel("RMSD (nm)", fontsize=12)
plt.legend(frameon=False, fontsize=12)

plt.xlim(-2, 102)

plt.tight_layout()
plt.savefig("Combined_RMSD_corrected.png", dpi=300)
plt.savefig("Combined_RMSD_corrected.pdf", dpi=300)
plt.show()
