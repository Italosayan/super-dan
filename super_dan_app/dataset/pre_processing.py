"""
Prepare for training the data requested by get_data.py
"""
import pandas as pd
import os


def data_pre_processing(df: pd.DataFrame) -> pd.DataFrame:
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
    temp_file = "queried_data/2019-11-19|09:59:41.089914_crimes.csv"
    # Path of pre_processing.py
    file = os.path.realpath(__file__)
    # Get the directory where pre_processing is
    dir_path = os.path.dirname(file)
    # Join the temp file with the dir
    conf_path = os.path.join(dir_path, temp_file)

    data_frame_roc_crimes = pd.read_csv(conf_path)

    return data_pre_processing(data_frame_roc_crimes)


if __name__ == '__main__':
    main()
