import my_utils as mt
import sys

file_name = sys.argv[1]
country = sys.argv[2]
country_column = 1
fires_column = 4
fires = mt.get_column(file_name, country_column, country,
                      result_column=fires_column)
print(fires)
