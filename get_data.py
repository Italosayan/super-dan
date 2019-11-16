import requests
import json
from datetime import datetime


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

rochester_crime_data = requests.get(REQUEST_URL)
rochester_crime_data = json.loads(rochester_crime_data.content)

now = datetime.now()

employ_data = open('./S3_Responses/.csv', 'w')

rochester_crime_data['features'][0]['geometry']['x']
rochester_crime_data['features'][0]['geometry']['y']
rochester_crime_data['features'][0]['attributes']
