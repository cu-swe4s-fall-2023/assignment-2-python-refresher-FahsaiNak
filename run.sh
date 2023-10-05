#!/bin/bash
#set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

echo "Program is running"
python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 4
python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 4 --operation mean
python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 4 --operation median
python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 4 --operation std
python print_fires.py --file_name Agrofood_o2_emission.csv --country "United States of America" --fires_column 4
python print_fires.py --file_name Agrofood_co2_emission.csv --country "Bermuda" --fires_column 11 --operation mean
echo "Done"
