# Assignment 3: Best Practices

## About the Project

## Getting started

### Prerequisites

* Install Conda [Conda](https://conda.io/projects/conda/en/latest/user-guide/install/index.html)

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

3. Excute print_fires.py to prints out a number of fire events in a specified country
   ```sh
   python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 3
   ```
   An example of output
   ```console
   A number of fires from Savanna fires in United States of America is 31
   ```

### Usage Example

The file named run.sh includes three examples of running print_fires.py, one that works and two that give errors as shown below

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


1. Completed the implementation of get_column() in my_utils.py as following:
   
   i.  Let the function open the file named file_name and operate it line by line.

   ii. Split each line into an array.

   iii. Check a condition, if the value in the query_column position of the array matches the value stored in the query_value variable, the function will add the value in the result_column position to a result array.

   iv. Return the result array storing the column values with the column headers.

   v. The function uses a named argument only for the result_column variable (default = 1).

2. Updated print_fires.py to proceed the get_column() function from my_utils.py and print out the number of fire events occurred in any defined country from 1990-2020.

3. Created run.sh that runs print_fires.py based on the specified file name, the name of country and the column number of fire events in the script. With all required parameters assigned, the run prints out a number of fire events in a specific country as shown below.
   ```sh
   python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 3
   ```
   An example of output
   ```console
   A number of fires from Savanna fires in United States of America is 31
   ```
