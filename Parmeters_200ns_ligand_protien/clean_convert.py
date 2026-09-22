import sys

def xpm_to_dat(xpm_file, dat_file):
    with open(xpm_file, 'r') as f:
        lines = f.readlines()

    # 1. Parse Dimensions
    meta_line = [l for l in lines if l.startswith('"') and len(l.split()) >= 4][0]
    meta = meta_line.replace('"', '').replace(',', '').split()
    cpp = int(meta[3])

    # 2. Build the color-to-value map (grabbing the ACTUAL number)
    color_map = {}
    for line in lines:
        if '/*' in line and '*/' in line and '"' in line:
            # This looks for: /* "char" value */
            parts = line.replace('/*', '').replace('*/', '').replace('"', '').split()
            if len(parts) >= 2:
                char = parts[0]
                val = parts[1]
                color_map[char] = val

    # 3. Extract matrix data
    data = []
    for line in lines:
        if line.startswith('"') and not any(x in line for x in ['+', 'static', '/*']):
            if len(line.split()) < 3: 
                row_str = line.strip('" \n,;')
                try:
                    # Convert the characters into the numerical values from our map
                    row_vals = [color_map[row_str[i:i+cpp]] for i in range(0, len(row_str), cpp)]
                    data.append(" ".join(row_vals))
                except KeyError:
                    continue

    with open(dat_file, 'w') as out:
        out.write("\n".join(data[::-1]))
    print(f"Fixed! {dat_file} now contains numbers.")

if __name__ == "__main__":
    xpm_to_dat(sys.argv[1], sys.argv[2])
