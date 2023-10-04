def get_column(file_name, query_column, query_value, result_column=1):
    """
    Extracts data from a CSV file based on a query and returns a list of values from a specified result column.

    Args:
    - file_name (str): The name of the CSV file to read.
    - query_column (int): The column index (1-based) to use as the query condition.
    - query_value (str): The value to search for in the specified query column.
    - result_column (int, optional): The column index (1-based) from which to extract values. Default is 1.

    Returns:
    - result (list): A list of values from the specified result column that match the query condition.

    Note:
    - The function assumes that the CSV file has a header row.
    - The column indices are 1-based, where 1 corresponds to the first column.
    """
    # If something wrong in opening the file, the function returns None
    try:
        f = open(file_name, 'r')
    except FileNotFoundError:
        print('Could not find', file_name)
        return None
    except PermissionError:
        print('Could not open', file_name)
        return None
    result = list()
    for ind, line in enumerate(f):
        array = line.rstrip().split(',')
        query = array[query_column-1]
        if query == query_value:
            try:
                result.append(int(float(array[result_column-1])))
            except ValueError:
                continue
    f.close()
    return result


def calculate_mean(lst):
    return round(sum(lst)/len(lst), 2)


def calculate_median(lst):
    n = len(lst)
    lst.sort()
    if n % 2 == 0:
        median1 = lst[n//2]
        median2 = lst[n//2 - 1]
        median = (median1 + median2)/2
    else:
        median = lst[n//2]
    return round(median, 2)


def calculate_std_dev(lst):
    mean = calculate_mean(lst)
    variance = sum((xi - mean) ** 2 for xi in lst) / len(lst)
    std_dev = variance ** 0.5
    return round(std_dev, 2)
