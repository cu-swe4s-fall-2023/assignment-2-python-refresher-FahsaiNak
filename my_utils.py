def get_column(file_name, query_column, query_value, result_column=1):
    result = list()
    with open(file_name,'r') as f:
        for line in f:
            array = line.rstrip().split(',')
            query = array[query_column-1]
            if query == query_value:
                result.append(float(array[result_column-1]))
    return result