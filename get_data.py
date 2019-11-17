import requests
import json
from datetime import datetime
import pandas as pd

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

REQUEST_URL = URL_CRIME_60_DAYS + FIELDS_STRING + ",".join(FIELDS) + OUTPUT_FORMAT


def crime_request_to_dict(url):
    """
    :param url: Format to access the rpdny API
    https://data-rpdny.opendata.arcgis.com/datasets/rpd-part-i-crime-60-days/geoservice

    :return: Python dictionary of 60 days of crime data.
    """
    rochester_crime_data = requests.get(url)
    rochester_crime_data = json.loads(rochester_crime_data.content)

    return rochester_crime_data


def dict_to_data_frame(dict_data):
    """
    :param dict_data: Request response in dictionary format
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

    attributes = [i['attributes'] if 'attributes' in i else empty_attr for i in dict_data['features']]
    geometry = [i['geometry'] if 'geometry' in i else empty_geometry for i in dict_data['features']]

    attributes = pd.DataFrame(attributes)
    geometry = pd.DataFrame(geometry)

    data_frame_of_crimes = pd.concat([attributes, geometry], axis=1, sort=False)

    return data_frame_of_crimes


def main():
    """
    This file requests the rochester crime data to the RPD-NY API.
    Then, formats the return to a consumable format.
    """
    roc_crimes = crime_request_to_dict(REQUEST_URL)
    data_frame_roc_crimes = dict_to_data_frame(roc_crimes)
    now = str(datetime.now())
    # TODO: Save data to S3 Bucket
    return now, data_frame_roc_crimes


if __name__ == '__main__':
    main()
