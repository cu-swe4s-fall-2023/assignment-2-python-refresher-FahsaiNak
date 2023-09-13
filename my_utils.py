def get_column(file_name, query_column, query_value, result_column=1):
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
