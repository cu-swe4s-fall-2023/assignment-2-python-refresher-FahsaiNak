import my_utils
from collections import namedtuple
import argparse


def get_args():
    parser = argparse.ArgumentParser(
        description = 'Print a number of fires in a specified country',
        prog = 'print_fires')
    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)
    parser.add_argument('--country', type=str,
                        help='Name of the country', required=True)
    parser.add_argument('--fires_column', type=int,
                        help='The column number of the fires', required=True)
    parser.add_argument('--country_column', type=int, default=1,
                        help='The column number of the country name')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    args.country_column = 1
    fires = my_utils.get_column(args.file_name, args.country_column, args.country, result_column=args.fires_column)
    num_fires = len([val for val in fires[1:] if val != 0])
    print(f"A number of fires from {fires[0]} in {args.country} is {num_fires}")


if __name__ == '__main__':
    main()
    