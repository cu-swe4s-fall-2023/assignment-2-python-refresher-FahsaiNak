#!/bin/bash
#set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

python get_data.py --file_name Agrofood_co2_emission.csv --country "China" --fire_column 5 --out_file China.5.txt
python get_data.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fire_column 5 --out_file "United States of America.5.txt"
python hist.py --data_file_1 China.5.txt --data_file_2 "United States of America.5.txt" --out_file hist_5.png --title "CO2 emission from Crop Residues in China and United States of America" --x "CO2 emission" --y "Counts"
