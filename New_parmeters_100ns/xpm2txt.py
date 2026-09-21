import sys

def convert_xpm_to_txt(infile, outfile):
    x_coords = []
    y_coords = []
    data = []
    
    with open(infile, 'r') as f:
        lines = f.readlines()

    # Find where the actual image data starts (after the color definitions)
    # XPM data lines are enclosed in quotes and usually follow a /* pixels */ comment
    start_idx = 0
    for i, line in enumerate(lines):
        if "/* pixels */" in line:
            start_idx = i + 1
            break
    
    if start_idx == 0: # Fallback if comment is missing
        for i, line in enumerate(lines):
            if line.startswith('"') and len(line) > 100:
                start_idx = i
                break

    pixel_lines = [l.strip().strip('",') for l in lines[start_idx:] if l.startswith('"')]

    with open(outfile, 'w') as f_out:
        for y, row in enumerate(pixel_lines):
            for x, char in enumerate(row):
                # Convert char to numeric value (ASCII)
                # Note: Real FES scripts map colors to energy, 
                # but this gets the shape into Pandas.
                f_out.write(f"{x}\t{y}\t{ord(char)}\n")

convert_xpm_to_txt("FES.xpm", "free-energy-landscape.txt")
print("Done! File saved as free-energy-landscape.txt")
