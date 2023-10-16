import sys
import argparse
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
        description='Get Crop Residues of the specified country',
        prog='get_fires')
    parser.add_argument('--file_name', type=str,
                        help='Name of the file', required=True)
    parser.add_argument('--country', type=str,
                        help='Name of the selected country', required=True)
    parser.add_argument('--out_file', type=str,
                        help='Name of the output file', required=True)
    parser.add_argument('--country_column', type=int,
                        help='The column number of the country name', default=1)
    parser.add_argument('--fire_column', type=int,
                        help='The column number of the country name')
    args = parser.parse_args()
    return args


def main():
    args = get_args()
    fires = my_utils.get_column(args.file_name, args.country_column,
                                args.country, result_column=args.fire_column)
    if fires is None:
        sys.exit(1)
    else:
        with open(args.out_file, 'w') as f:
            for val in fires:
                f.write(str(val)+'\n')


if __name__ == '__main__':
    main()
