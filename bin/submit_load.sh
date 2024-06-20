#!/bin/bash
#SBATCH -A b1119
#SBATCH -p posydon-priority                # Queue
#SBATCH -t 00:10:00             # Walltime/duration of the job
#SBATCH -N 1                    # Number of Nodes
#SBATCH --mem=4G               # Memory per node in GB needed for a job. Also see --mem-per-cpu
#SBATCH --ntasks-per-node=4     # Number of Cores (Processors)
#SBATCH --mail-type=ALL
#SBATCH --mail-user=elizabethteng@u.northwestern.edu
#SBATCH --output="mat.out"

source activate /projects/b1119/briel/software/loadv2_env_240618

python load_pop.py --gridfile "IF/burstSFR/alpha_0.2/1e+00_Zsun_population.h5"