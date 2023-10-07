# Assignment 5: Continuous Integration

## About the Project

A program that prints out the operated number of fire events occurred in any defined country from 1990-2020.

## Getting started

### Prerequisites

* Install [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

* Install python 3.x

* Install argparse
  ```sh
  pip install argparse
  ```

* Install sys
  ```sh
  pip install sys
  ```

* To run unit/functional test: unittest, random, os and numpy are required.

### Installation

1. Clone the repository
   ```sh
   git clone https://github.com/cu-swe4s-fall-2023/assignment-2-python-refresher-FahsaiNak.git
   ```

2. Get a data file named "Agrofood_co2_emission.csv" from the classroom google drive [Link](https://drive.google.com/drive/u/3/folders/15dnNnOEjDZDvwzM-_tGGtWjTbNL669i7) and place in the root directory of the repository

3. Excute print_fires.py to prints out a number of fire events in a specified country. The program requires parameters as following:
   - The specified CSV file name (--file_name)
   - The column number of the fire event (--fires_column)
   - The name of the country (--country)
   - (Optional) The column number of the country (--country_column)
   - (Optional) The operation to perform: mean, median, std (--operation)
   
   Running command example:
   ```sh
   python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 4 --operation mean
   ```
   Output example:
   ```console
   United States of America operated with mean 1928.23
   ```

### Usage Example

The file named run.sh includes some examples of running print_fires.py that works and gives errors:

   ```sh
   ./run.sh
   ```

### Summary of Changes

Created a automated testing file (tests.yml) in the Github workflow that runs whenever a push or pull requests to the main branch
