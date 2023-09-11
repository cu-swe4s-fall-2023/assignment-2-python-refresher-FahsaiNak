[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oQi7O4AA)
# Summary of changes
1. Completed the implementation of get_column() in my_utils.py as following:
   
   i.  Let the function open the file named file_name and operate it line by line.
   ii. Split each line into an array.
   iii. Check a condition, if the value in the query_column position of the array matches the value stored in the query_value variable, the function will add the value in the result_column position to a result array.
   iv. Return the result array storing the column values.
   v. The function uses a named argument only for the result_column variable (defult = 1).

2. Updated print_fires.py to proceed the get_column() function from my_utils.py and print out the number of fires in any defined country.

3. Created run.sh that runs print_fires.py based on the specified file name and the country of interest in the script.
