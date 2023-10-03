import my_utils
import argparse
import sys


def get_args():
    """
    Parse command-line arguments for the script.

    Returns:
    - argparse.Namespace: An object containing the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Print a number of fires in a specified country with/without operation',
        prog='print_fires')
    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)
    parser.add_argument('--country', type=str,
                        help='Name of the country', required=True)
    parser.add_argument('--fires_column', type=int,
                        help='The column number of the fires', required=True)
    parser.add_argument('--country_column', type=int, default=1,
                        help='The column number of the country name')
    parser.add_argument('--operation', type=str, default=None,
                        help='The operation to perform: mean, median, std')    
    args = parser.parse_args()
    return args


def main():
    """
    Main function of the script. Extracts fire data and prints the number of fires in a specified country.
    """
    args = get_args()
    fires = my_utils.get_column(args.file_name, args.country_column,
                                args.country, result_column=args.fires_column)
    if fires is None:
        sys.exit(1)
    else:
        if args.operation == None:
            val = fires
        elif args.operation == "mean":
            val = my_utils.calculate_mean(fires)
        elif args.operation == "median":
            val = my_utils.calculate_median(fires)
        elif args.operation == "std":
            val = my_utils.calculate_std_dev(fires)
        else:
            print("The assigned --operation is not matched; either mean, median or std is provided.")
            sys.exit(1)
    print("Operation:", args.operation, val)


if __name__ == '__main__':
    main()
