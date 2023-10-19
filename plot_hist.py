import sys
import argparse
import matplotlib
import matplotlib.pyplot as plt
sys.path.insert(0, 'src')
import my_utils  # noqa


def get_args():
    """
    Parse command-line arguments for the script.

    Returns:
    - argparse.Namespace: An object containing
    the parsed command-line arguments.
    """
    parser = argparse.ArgumentParser(
        description='Compare fires of the two countries',
        prog='hist_fires')
    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)
    parser.add_argument('--country_1', type=str,
                        help='Name of country 1', required=True)
    parser.add_argument('--country_2', type=str,
                        help='Name of country 2', required=True)
    parser.add_argument('--fire_column', type=int,
                        help='The column number of the fire event')
    parser.add_argument('--country_column', type=int,
                        help='The column number of the country name',
                        default=1)
    parser.add_argument('--out_file', type=str,
                        help='Name of the output file', required=True)
    parser.add_argument('--title', type=str,
                        help='Title of the histrogram', required=True)
    parser.add_argument('--x', type=str,
                        help='Name of the X-axis in the histogram',
                        required=True)
    parser.add_argument('--y', type=str,
                        help='Name of the y-axis in the histogram',
                        required=True)
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    D1 = my_utils.get_column(args.file_name, args.country_column,
                             args.country_1, result_column=args.fire_column)
    D2 = my_utils.get_column(args.file_name, args.country_column,
                             args.country_2, result_column=args.fire_column)
    if D1 is None:
        sys.exit(1)
    elif D2 is None:
        sys.exit(1)
    else:
        plt.hist(D1, label=args.country_1,
                 alpha=.7, color='red')
        plt.hist(D2, label=args.country_2,
                 alpha=.7, color='yellow')
        plt.legend()
        plt.xlabel(args.x)
        plt.ylabel(args.y)
        plt.title(args.title)
        plt.savefig(args.out_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
