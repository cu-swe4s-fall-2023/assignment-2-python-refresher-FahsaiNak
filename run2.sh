#!/bin/bash
#set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

COUNTRIES=("China" "United States of America")
FRIES=(4 5 6)

for fire in ${FRIES[@]}; do
    for country in "${COUNTRIES[@]}"; do
        python get_data.py --file_name Agrofood_co2_emission.csv --country "${country}" --fire_column $fire --out_file "${country}.$fire.txt";
    done;
    file_1="${COUNTRIES[0]}.$fire.txt"
    file_2="${COUNTRIES[1]}.$fire.txt"
    python hist.py --data_file_1 "${file_1}" --data_file_2 "${file_2}" --out_file hist_$fire.png --title "CO2 emission from fire column $fire" --x "CO2 emission" --y "Counts";
done
