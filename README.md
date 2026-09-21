# GROMACS Molecular Dynamics Workflow

This repository contains GROMACS molecular dynamics simulation commands, parameter files, analysis scripts, and documentation for protein, protein–ligand, mutant-versus-wild-type, and Vaccine–TLR4 systems.

## General MD Workflow

1. Prepare the protein and ligand structures.
2. Generate the protein topology using the appropriate force field.
3. Generate ligand parameters using CGenFF when required.
4. Construct and verify the protein–ligand complex.
5. Create a cubic simulation box.
6. Solvate the system with TIP3P water.
7. Add ions and neutralize the system.
8. Perform energy minimization.
9. Perform NVT equilibration.
10. Perform NPT equilibration.
11. Run the production MD simulation.
12. Remove periodic boundary conditions and fit the trajectory.
13. Perform RMSD, RMSF, radius of gyration, SASA, hydrogen-bond, PCA, FEL, DCCM, and MM/PBSA analyses.

## Simulation Templates

* Protein in water: 200 ns
* Protein–ligand complex: 100 ns
* Protein–ligand complex: 200 ns
* Mutant versus wild type: 100 ns
* Vaccine–TLR4 complex: 100 ns with three replicates

## Repository Organization

* `workflows/` — GROMACS workflow shell scripts
* `parameters/` — EM, ion, NVT, NPT, MD, and MM/PBSA parameter files
* `analysis/` — trajectory-analysis and plotting scripts
* `utilities/` — ligand preparation and file-conversion utilities
* `docs/` — detailed command notes and documentation
* `original_files/` — preserved original workflow files

## Important Notes

The numerical index-group selections displayed by GROMACS may differ between systems. Always confirm the group name before selecting it.

Large simulation outputs such as `.xtc`, `.trr`, `.tpr`, `.edr`, `.cpt`, and log files should not be uploaded to GitHub.

Production duration must be confirmed using:

```text
Simulation time = nsteps × dt
```

For a 2 fs timestep:

* 50,000,000 steps = 100 ns
* 100,000,000 steps = 200 ns

## Software

* GROMACS
* CHARMM36 or AMBER99SB-ILDN
* TIP3P water
* CGenFF for ligand parameterization
* gmx_MMPBSA
* Python for plotting and post-processing

## Author

Hayat Khan
Genomics and Bioinformatics
North Dakota State University
