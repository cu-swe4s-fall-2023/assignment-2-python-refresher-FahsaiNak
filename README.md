# Assignment 3: Best Practices

## About the Project

A program that prints out the number of fire events occurred in any defined country from 1990-2020.

## Getting started

### Prerequisites

* Install [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

* Install argparse
  ```sh
  pip install argparse
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
   
   Running command example:
   ```sh
   python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 3
   ```
   Output example:
   ```console
   A number of fires from Savanna fires in United States of America is 31
   ```

### Usage Example

The file named run.sh includes three examples of running print_fires.py, one that works and two that give errors as shown below:

   ```sh
   ./run.sh
   ```
    
   ```console
    Program is running
    A number of fires from Savanna fires in United States of America is 31
    Could not find Agrofood_o2_emission.csv
    Some values in the column 11 : Net Forest conversion of Bermuda are not numbers, potentailly no value
    Done
   ```
