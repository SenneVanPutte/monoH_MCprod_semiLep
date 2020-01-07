#!/bin/bash

mass_points=(
    MH3_1200_MH4_150_MH2_1200_MHC_1200
    MH3_200_MH4_150_MH2_200_MHC_200 
    MH3_300_MH4_150_MH2_300_MHC_300 
    MH3_400_MH4_150_MH2_400_MHC_400 
    MH3_500_MH4_150_MH2_500_MHC_500 
    MH3_600_MH4_150_MH2_600_MHC_600
)

sngs=(
    pos 
    neg
)

for mp in "${mass_points[@]}"
do
    echo "$mp"
    for sng in "${sngs[@]}"
    do
        echo "$sng"
        python crab_cfg_step2.py --mp=$mp --sng=$sng 
    done
done

 
