"""
Prepare for training the data requested by get_data.py
"""
from pathlib import Path
import pandas as pd


def na_values(df: pd.DataFrame) -> pd.DataFrame:
    """
    Remove NA values of data frame
    """
    return df.dropna()


def dummy_location_type_variable(df: pd.DataFrame) -> pd.DataFrame:
    """
    Turning the location type into
    multiple dummy variables.
    """
    location_types = ["Single Family Home",
                      "Other Outside Location",
                      "Multiple Dwelling",
                      "Street",
                      "Parking Lot"]

    df.loc[~df['Location_Type'].isin(location_types), 'Location_Type'] = "Other"
    dummy_locations = pd.get_dummies(df.loc[:, "Location_Type"])
    df = pd.concat([df, dummy_locations], axis=1).drop(columns="Location_Type")

    return df


def setting_features_and_target(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean statute text. Statute Text will be the target variable.
    Filter columns and return clean dataset

    :param df: raw data from get_data
    """
    # Preprocess target variable
    df = df[df['Statute_Text'].isin(["Larceny", "Burglary"])]

    # Filter interesting columns
    cols = ['OccurredFrom_Timestamp',
            'OccurredThrough_Timestamp',
            'Reported_Timestamp',
            'Location_Type',
            'x', 'y',
            'Statute_Text']

    return df[cols]


def read_data() -> pd.DataFrame:
    """
    Read data from queried_data/
    :return: read csv
    """
    temp_data_dir = "queried_data/"
    dataset_module_path = Path(__file__).parent
    data_dir = dataset_module_path / temp_data_dir

    all_csv = list(data_dir.glob('*.csv'))
    first_csv = str(all_csv[0])
    data_frame_roc_crimes = pd.read_csv(first_csv)

    return data_frame_roc_crimes


def main():
    """
    Prepare for training the data requested by get_data.py
    :return: Data frame ready for training
    """

    data_frame_roc_crimes = read_data()
    features_target = setting_features_and_target(data_frame_roc_crimes)
    features_target = dummy_location_type_variable(features_target)
    features_target = na_values(features_target)

    return features_target


if __name__ == '__main__':
    main()
