#!/bin/bash

mass_points=(
    "mhs_160_mx_100_mZp_1000"
    "mhs_160_mx_100_mZp_1200"
    "mhs_160_mx_100_mZp_1500"
    "mhs_160_mx_100_mZp_195"
    "mhs_160_mx_100_mZp_250"
    "mhs_160_mx_100_mZp_295"
    "mhs_160_mx_100_mZp_300"
    "mhs_160_mx_100_mZp_500"
    "mhs_160_mx_150_mZp_1000"
    "mhs_160_mx_150_mZp_1500"
    "mhs_160_mx_150_mZp_195"
    "mhs_160_mx_150_mZp_250"
    "mhs_160_mx_150_mZp_295"
    "mhs_160_mx_150_mZp_300"
    "mhs_160_mx_200_mZp_1200"
    "mhs_160_mx_200_mZp_250"
    "mhs_160_mx_200_mZp_295"
    "mhs_160_mx_200_mZp_300"
    "mhs_160_mx_200_mZp_500"
    "mhs_180_mx_100_mZp_1000"
    "mhs_180_mx_100_mZp_1200"
    "mhs_180_mx_100_mZp_1500"
    "mhs_180_mx_100_mZp_195"
    "mhs_180_mx_100_mZp_250"
    "mhs_180_mx_100_mZp_295"
    "mhs_180_mx_100_mZp_300"
    "mhs_180_mx_100_mZp_500"
    "mhs_180_mx_150_mZp_1000"
    "mhs_180_mx_150_mZp_1500"
    "mhs_180_mx_150_mZp_195"
    "mhs_180_mx_150_mZp_295"
    "mhs_180_mx_150_mZp_500"
    "mhs_180_mx_200_mZp_1200"
    "mhs_180_mx_200_mZp_1500"
    "mhs_180_mx_200_mZp_195"
    "mhs_180_mx_200_mZp_250"
    "mhs_180_mx_200_mZp_295"
    "mhs_180_mx_200_mZp_300"
    "mhs_180_mx_200_mZp_500"
    "mhs_200_mx_100_mZp_1000"
    "mhs_200_mx_100_mZp_1500"
    "mhs_200_mx_100_mZp_250"
    "mhs_200_mx_100_mZp_300"
    "mhs_200_mx_150_mZp_1000"
    "mhs_200_mx_150_mZp_1200"
    "mhs_200_mx_150_mZp_1500"
    "mhs_200_mx_150_mZp_250"
    "mhs_200_mx_150_mZp_300"
)

sngs=(
    "pos" 
    "neg"
)

for mp in "${mass_points[@]}"
do
    echo "$mp"
    for sng in "${sngs[@]}"
    do
        echo "$sng"
        #python crab_cfg_step0.py --mp=$mp --sng=$sng 
    done
done

 
