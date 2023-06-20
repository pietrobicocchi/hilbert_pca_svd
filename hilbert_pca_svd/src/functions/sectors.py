import numpy as np
import pandas as pd
from typing import Tuple, List, Dict


def create_GICS_dict():
    """
    Creates a dictionary that maps GICS two-digit codes to their corresponding sector names.

    Returns:
    dict: A dictionary mapping GICS codes to sector names.
    """

    GICS = {}
    gsects = [1.0, 10., 15., 20., 25., 30., 35., 40., 45., 50., 55., 60.]
    sects = ["Other", "Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", "Health Care", "Financials",
             "Information Technology", "Communication Services", "Utilities", "Real Estate"]

    for i in range(len(gsects)):
        GICS[gsects[i]] = sects[i]

    return GICS


def get_unique_sectors(sectors):
    """
    Extracts unique GVKEY and their associated maj_sector from the sectors DataFrame.

    Args:
    sectors (pandas.DataFrame): DataFrame containing columns 'GVKEY', 'datadate', and 'gsector'.

    Returns:
    pandas.DataFrame: DataFrame containing unique GVKEY and their associated maj_sector.
    """
    GICS = create_GICS_dict()
    sectors = sectors[['GVKEY', 'datadate', 'gsector']]
    sectors["datadate"] = pd.to_datetime(sectors["datadate"])
    sectors['gsector'] = sectors['gsector'].fillna(1)
    sectors['maj_sector'] = sectors.groupby('GVKEY')['gsector'].transform(lambda x: x.mode().iat[0])
    unique_sectors = sectors[['GVKEY', 'maj_sector']].drop_duplicates()
    unique_sectors['sector_name'] = unique_sectors['maj_sector'].map(GICS)
    unique_sectors = unique_sectors.set_index('GVKEY')

    return unique_sectors


def gvkeys_to_sect(gvkeys: List[str], unique_sectors) -> List[str]:
    """
    Retrieves the sector information for a list of gvkeys and returns a list of corresponding sectors.
    """

    key_sect = []

    for key in gvkeys:
        try:
            sec = unique_sectors.loc[key]['sector_name']
            key_sect.append(sec)
        except KeyError:
            # Handle the KeyError condition here
            key_sect.append('Other')  # 'Other' added as a default value to the list

    return key_sect


def create_sectors(key_sect: List[str]) -> Tuple[np.ndarray, Dict[str, List[int]], List[int], List[str]]:
    """
    Creates sector indices and labels based on a list of ticker sectors.

    Args:
        key_sect (List[str]): A list of sectors assigned to each ticker.

    Returns:
        Tuple[np.ndarray, Dict[str, List[int]], List[int], List[str]]: A tuple containing the following:
            - idx_by_sector (np.ndarray): An array of indices representing the sectors sorted in ascending order.
            - sector_dict (Dict[str, List[int]]): A dictionary mapping each sector to a list of corresponding indices.
            - sector_indices (List[int]): A list of sector indices corresponding to the ticker sectors.
            - sector_labels (List[str]): A list of sector labels.

    Raises:
        None

    Example:
        key_sect = ['Technology', 'Financial', 'Technology', 'Healthcare', 'Financial']

        idx_by_sector, sector_dict, sector_indices, sector_labels = sectors(key_sect)
    """

    idx_by_sector = np.argsort(key_sect)  # tick is my list that assign at each ticker the corresponding sector

    # create dictionary mapping sectors to tickers
    sector_dict = {}
    for i in range(len(key_sect)):
        sector = key_sect[i]
        if sector not in sector_dict:
            sector_dict[sector] = []
        sector_dict[sector].append(i)

    # sort sector names alphabetically
    sector_names = sorted(sector_dict.keys())

    # create list of sector labels and corresponding indices
    sector_labels = []
    sector_indices = []
    for sector in sector_names:
        sector_labels.append(sector)
        for i in idx_by_sector:
            if i in sector_dict[sector]:
                sector_indices.append(idx_by_sector.tolist().index(i) + 1)  # +1 just to translate it graphically
                break
    return idx_by_sector, sector_dict, sector_indices, sector_labels

