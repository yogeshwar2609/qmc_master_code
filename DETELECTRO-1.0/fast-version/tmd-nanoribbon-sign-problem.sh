#!/bin/bash

#cd ~/qmc_master_code/DETELECTRO-1.0/fast-version/

make source=mainSignProblem clean

make nsites=$1 beta=$2 source="mainSignProblem" U=$3

for i in $(eval echo {1..$4})
  do

    ./simulation_mainSignProblem_nsites$1_dt_inv16_beta$2_green_afresh_freq4_U_$3 1 $3 $(echo 0.3*$i - 0.3 | bc) 15 $5 $6 $7 $8

    cd results

    echo "Saving simulation data"

    python3 save-sign.py

    cd ../

  done
