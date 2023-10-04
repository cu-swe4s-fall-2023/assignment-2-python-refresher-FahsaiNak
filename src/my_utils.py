def get_column(file_name, query_column, query_value, result_column=1):
    """
    Extracts numeric values from a specified column in a CSV file based on a query in another column.

    Parameters:
    - file_name (str): The name of the CSV file to read.
    - query_column (int): The column number (1-based index) to use as a query filter.
    - query_value (str): The value to search for in the specified query_column.
    - result_column (int, optional): The column number (1-based index) from which to extract numeric values.
      Defaults to 1 if not specified.

    Returns:
    - result (list): A list of numeric values from the specified result_column
      where the query_column matches the query_value.
    """
    try:
        f = open(file_name, 'r')  # Open the CSV file for reading.
    except FileNotFoundError:
        print('Could not find', file_name)
        return None
    except PermissionError:
        print('Could not open', file_name)
        return None
    
    result = list()  # Initialize an empty list to store the result.
    
    for ind, line in enumerate(f):
        array = line.rstrip().split(',')  # Split each line by ',' to get columns.
        query = array[query_column-1]  # Get the value in the query_column.
        
        if query == query_value:  # Check if the query value matches the specified value.
            try:
                result.append(int(float(array[result_column-1])))  # Extract numeric data from result_column.
            except ValueError:
                continue  # Skip if the value in result_column is not numeric.
    
    f.close()  # Close the file.
    return result  # Return the list of extracted numeric values.


def calculate_mean(lst):
    """
    Calculates the mean (average) of a list of numeric values.

    Parameters:
    - lst (list): The list of numeric values for which you want to calculate the mean.

    Returns:
    - mean (float): The mean (average) value of the input list rounded to two decimal places.
    """
    return round(sum(lst) / len(lst), 2)


def calculate_median(lst):
    """
    Calculates the median of a list of numeric values.

    Parameters:
    - lst (list): The list of numeric values for which you want to calculate the median.

    Returns:
    - median (float): The median value of the input list rounded to two decimal places.
    """
    n = len(lst)
    lst.sort()
    if n % 2 == 0:
        median1 = lst[n//2]
        median2 = lst[n//2 - 1]
        median = (median1 + median2) / 2
    else:
        median = lst[n//2]
    return round(median, 2)


def calculate_std_dev(lst):
    """
    Calculates the standard deviation of a list of numeric values.

    Parameters:
    - lst (list): The list of numeric values for which you want to calculate the standard deviation.

    Returns:
    - std_dev (float): The standard deviation of the input list rounded to two decimal places.
    """
    mean = calculate_mean(lst)  # Calculate the mean.
    variance = sum((xi - mean) ** 2 for xi in lst) / len(lst)  # Calculate the variance.
    std_dev = variance ** 0.5  # Calculate the standard deviation.
    return round(std_dev, 2)