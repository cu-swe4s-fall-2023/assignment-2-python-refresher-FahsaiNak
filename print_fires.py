import my_utils
import sys
from collections import namedtuple


def main(var):
    fires = my_utils.get_column(var.file_name, var.country_column,
                                var.country, result_column=var.fires_column)
    num_fires = len([val for val in fires if val != 0])-1
    print("A number of", fires[0], "in", country, "is", num_fires)


if __name__ == '__main__':
    country = "United States of America"
    country_column = 1
    fires_column = 4
    file_name = "Agrofood_co2_emission.csv"
    Args = namedtuple('Args', ['file_name', 'country',
                               'country_column', 'fires_column'])
    Info = Args(file_name, country, country_column, fires_column)
    main(Info)
