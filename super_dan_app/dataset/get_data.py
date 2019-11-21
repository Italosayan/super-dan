"""
This file requests crime data to the RPD-NY API.
Then turns the response to a consumable format(pandas dataframe).
"""
import requests
import json
from datetime import datetime
import pandas as pd
import os

URL_CRIME_60_DAYS = "https://maps.cityofrochester.gov" \
                    "/arcgis/rest/services/RPD" \
                    "/RPD_Part_I_Crime/FeatureServer/2/query?where=1%3D1"

FIELDS_STRING = "&outFields="

FIELDS = ["OBJECTID",
          "OccurredFrom_Timestamp",
          "OccurredThrough_Timestamp",
          "Reported_Timestamp",
          "Statute_Text",
          "Statute_Description",
          "Weapon_Description",
          "Larceny_Type",
          "Location_Type"]

OUTPUT_FORMAT = "&outSR=4326&f=json"

REQUEST_URL = URL_CRIME_60_DAYS \
              + FIELDS_STRING + \
              ",".join(FIELDS) + \
              OUTPUT_FORMAT


def crime_data_request(url: str) -> requests.Response:
    """
    This function uses the REQUEST_URL to request data from the RPD API
    :param url: Url format to access the RPD API
    https://data-rpdny.opendata.arcgis.com/datasets/rpd-part-i-crime-60-days/geoservice
    :return: requests.Response data of 60 days of crime data.
    """
    rpd_answer = requests.get(url)
    return rpd_answer


def request_to_data_frame(json_data: requests.Response) -> pd.DataFrame:
    """
    This function cleans the response of the RPD API and
    puts it in a pandas data frame.
    :param json_data: Request response in json format
    :return: pandas data frame of one crime per row.
    """
    empty_geometry = {'x': None,
                      'y': None}

    empty_attr = {'OBJECTID': None,
                  'OccurredFrom_Timestamp': None,
                  'OccurredThrough_Timestamp': None,
                  'Reported_Timestamp': None,
                  'Statute_Text': None,
                  'Statute_Description': None,
                  'Weapon_Description': None,
                  'Larceny_Type': None,
                  'Location_Type': None}

    dict_data = json.loads(json_data.content)
    attributes = [i['attributes'] if 'attributes' in i else empty_attr
                  for i in dict_data['features']]

    geometry = [i['geometry'] if 'geometry' in i else empty_geometry
                for i in dict_data['features']]

    attributes = pd.DataFrame(attributes)
    geometry = pd.DataFrame(geometry)

    data_frame_of_crimes = pd.concat([attributes, geometry],
                                     axis=1,
                                     sort=False)

    return data_frame_of_crimes


def main():
    """
    First request, then clean and write to csv.
    """
    # Request
    roc_crimes_response = crime_data_request(REQUEST_URL)
    # Clean
    data_frame_roc_crimes = request_to_data_frame(roc_crimes_response)
    # Save
    now = str(datetime.now()).replace(" ", "|")
    os.makedirs("super_dan_app/dataset/queried_data", exist_ok=True)
    file_path = f"super_dan_app/dataset/queried_data/{now}_crimes.csv"
    data_frame_roc_crimes.to_csv(file_path, index=False)
    return 0


if __name__ == '__main__':
    main()
