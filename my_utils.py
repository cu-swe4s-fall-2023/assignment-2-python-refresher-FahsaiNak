def get_column(file_name, query_column, query_value, result_column):
    result = list()
    with open(file_name,'r') as f:
        for ind,line in enumerate(f):
            array = line.rstrip().split(',')
            query = array[query_column-1]
            if query == query_value:
                print(array)
                result.append(array[result_column-1])
    return result