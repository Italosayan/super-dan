"""
Prepare for training the data requested by get_data.py
"""
import pandas as pd
from pathlib import Path

def data_pre_processing(df):
    """
    Clean statute text. It will be the target variable
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


def main():
    """
    Prepare for training the data requested by get_data.py
    :return:
    """
    temp_data_dir = "queried_data/"
    dataset_module_path = Path(__file__).parent
    data_dir = dataset_module_path / temp_data_dir

    # Get all csv inside queried_data/
    first_csv = list(data_dir.glob('*.csv'))
    first_csv = str(first_csv[0])

    data_frame_roc_crimes = pd.read_csv(first_csv)

    return data_pre_processing(data_frame_roc_crimes)


if __name__ == '__main__':
    main()
