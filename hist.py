import sys
import argparse
!pip install matplotlib
import matplotlib  # noqa
import matplotlib.pyplot as plt  # noqa
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
    parser.add_argument('--data_file_1', type=str,
                        help='Name of the file 1', required=True)
    parser.add_argument('--data_file_2', type=str,
                        help='Name of the file 2', required=True)
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
    D1 = my_utils.getListFromFile(args.data_file_1)
    D2 = my_utils.getListFromFile(args.data_file_2)
    if D1 is None:
        sys.exit(1)
    elif D2 is None:
        sys.exit(1)
    else:
        plt.hist(D1, label=args.data_file_1.split('.')[0],
                 alpha=.7, color='red')
        plt.hist(D2, label=args.data_file_2.split('.')[0],
                 alpha=.7, color='yellow')
        plt.legend()
        plt.xlabel(args.x)
        plt.ylabel(args.y)
        plt.title(args.title)
        plt.savefig(args.out_file, bbox_inches='tight')


if __name__ == '__main__':
    main()
