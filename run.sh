#!/bin/bash
set -e # stop on error
set -u # raise error if variable is unset
set -o pipefail # fail if any prior step failed

echo "Program running"
python print_fires.py Agrofood_co2_emission.csv "United States of America"
echo "Finished"
