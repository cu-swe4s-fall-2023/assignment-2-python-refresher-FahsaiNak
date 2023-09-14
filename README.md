[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# Summary of changes
0. Added the data file named "Agrofood_co2_emission.csv" from the classroom google drive [Link](https://drive.google.com/drive/u/3/folders/15dnNnOEjDZDvwzM-_tGGtWjTbNL669i7)

1. Completed the implementation of get_column() in my_utils.py as following:
   
   i.  Let the function open the file named file_name and operate it line by line.

   ii. Split each line into an array.

   iii. Check a condition, if the value in the query_column position of the array matches the value stored in the query_value variable, the function will add the value in the result_column position to a result array.

   iv. Return the result array storing the column values with the column headers.

   v. The function uses a named argument only for the result_column variable (default = 1).

2. Updated print_fires.py to proceed the get_column() function from my_utils.py and print out the number of fire events occurred in any defined country from 1990-2020.

3. Created run.sh that runs print_fires.py based on the specified file name, the name of country and the column number of fire events in the script. With all required parameters assigned, the run prints out a number of fire events in a specific country as shown below.
   ```console
   $ python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 3
   A number of fires from Savanna fires in United States of America is 31
   $ python print_fires.py --file_name Agrofood_co2_emission.csv --country "United States of America" --fires_column 24
   A number of fires from Fires in humid tropical forests in United States of America is 27
   ```
