#!/bin/bash

#PBS -l nodes=1:ppn=1
#PBS -l walltime=96:00:00
cd ~/qmc_master_code/DETELECTRO-1.0/fast-version/

make clean

make nsites=$1 beta=$2 eq_or_uneq=src/$5 object=src/$6

./simulation 1 $3 $4 1 0 10192 1024 4

cd results

echo "Saving simulation data"

python save-simulation-data.py
