import pickle
import pandas as pd
import os
cwd = os.getcwd() # Get the current working directory
parent_dir = os.path.dirname(cwd)
parpar_dir = os.path.dirname(parent_dir)


def save_cleaned_data(data, filepath):
    """
    Saves cleaned data to a file using pickle.

    Args:
        data: The cleaned data to be saved.
        filepath (str): The filepath where the data will be saved.

    Returns:
        None

    Raises:
        IOError: If there is an error in saving the data.

    Example:
        cleaned_data = ...

        save_cleaned_data(cleaned_data, 'path/to/save/data.pkl')
    """
    try:
        with open(filepath, 'wb') as f:
            pickle.dump(data, f)
    except IOError as e:
        raise IOError("Error saving data: " + str(e))


def load_cleaned_data(filepath):
    """
    Loads cleaned data from a file using pickle.

    Args:
        filepath (str): The filepath from where the data will be loaded.

    Returns:
        The loaded cleaned data.

    Raises:
        IOError: If there is an error in loading the data.

    Example:
        loaded_data = load_cleaned_data('path/to/load/data.pkl')
    """
    try:
        with open(filepath, 'rb') as f:
            data = pickle.load(f)
            return data
    except IOError as e:
        raise IOError("Error loading data: " + str(e))


def extract_data(data_path: str = None):
    """This function extracts the desired information from the data file given.

    Args:
        data_path (str, optional): Path where one can read experimental measurements. Defaults to None.
    Returns:
        Dataframe.
    """
    if data_path is None:
        # by default, data are stored in the data folder
        data_path = str(get_project_root()) + str(DATA_DIR) + "/CompStat/crsp_ccm_inventories_sales.csv"

    # read the data
    df = pd.read_csv(data_path)
    return df


if __name__ == "__main__":
    print("I'm extracting the cleaned, pre-processed data using pickle")
