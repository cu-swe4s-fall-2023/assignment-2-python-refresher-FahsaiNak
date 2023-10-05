# Assignment 4: Testing

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

* Added new functions to find the mean, median, and standard deviation of a list of integers to my_utils.py and moved the file to src directory
* Created unit tests (test_my_utils.py) in test/unit directory for all functions in my_utils.py including randomness and positive and negative cases
* Edited print_fires.py by adding operation variable
* Created a functional test (test_print_fires.sh) in test/functional directory to test print_fires.py, including exit codes and different operation cases
* Created a small test data file of the full data sets and checked into to test/functional directory
