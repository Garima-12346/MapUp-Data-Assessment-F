import pandas as pd


def generate_car_matrix(df)->pd.DataFrame:
    """
    Creates a DataFrame  for id combinations.

    Args:
        df (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Matrix generated with 'car' values, 
                          where 'id_1' and 'id_2' are used as indices and columns respectively.
    """
    # Write your logic here
    matrix = df.pivot(index='id_1', columns='id_2', values='car').fillna(0)
    return matrix
   


def get_type_count(df)->dict:
    """
    Categorizes 'car' values into types and returns a dictionary of counts.

    Args:
        df (pandas.DataFrame)

    Returns:
        dict: A dictionary with car types as keys and their counts as values.
    """
    # Write your logic here
    type_counts = df['car'].value_counts().to_dict()
    return type_counts



def get_bus_indexes(df)->list:
    """
    Returns the indexes where the 'bus' values are greater than twice the mean.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of indexes where 'bus' values exceed twice the mean.
    """
    # Write your logic here
    bus_indexes = df[df['car'] == 'bus'].index[df['car'] == 'bus'].tolist()
    mean_bus = df[df['car'] == 'bus']['value'].mean()
    bus_indexes_twice_mean = [index for index in bus_indexes if df.at[index, 'value'] > 2 * mean_bus]
    return bus_indexes_twice_mean



def filter_routes(df)->list:
    """
    Filters and returns routes with average 'truck' values greater than 7.

    Args:
        df (pandas.DataFrame)

    Returns:
        list: List of route names with average 'truck' values greater than 7.
    """
    avg_truck_values = df.groupby('route')['car'].mean()
    routes_greater_than_7 = avg_truck_values[avg_truck_values > 7].index.tolist()
    return routes_greater_than_7



def multiply_matrix(matrix)->pd.DataFrame:
    """
    Multiplies matrix values with custom conditions.

    Args:
        matrix (pandas.DataFrame)

    Returns:
        pandas.DataFrame: Modified matrix with values multiplied based on custom conditions.
    """
    # Write your logic here
    matrix[matrix > 5] *= 2
    return matrix
