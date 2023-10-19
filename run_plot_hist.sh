#!/bin/bash
#set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

COUNTRIES=("United States of America" "China")
FRIES=(4 5 6)

for fire in ${FRIES[@]}; do
    python plot_hist.py --file_name Agrofood_co2_emission.csv --country_1 "${COUNTRIES[0]}" --country_2 "${COUNTRIES[1]}" --fire_column $fire --out_file hist_$fire.png --title "CO2 emission from fire column $fire" --x "CO2 emission" --y "Counts";
done
