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
    with open(file_name, 'r') as f:
        for ind, line in enumerate(f):
            array = line.rstrip().split(',')
            if ind == 0:
                collection = [list(array)]
            query = array[query_column-1]
            if query == query_value:
                collection.append(array)
        result = [row[result_column-1] for row in collection]
    return result
