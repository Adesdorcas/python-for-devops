# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://emenoge-dorcas.atlassian.net/rest/api/3/project"

API_TOKEN="ATATT3xFfGF0ZW7BPaMqrveoOtz1ejwAgcrYPpGRhmPwoAg48MZRFFIRMWqhbvAAiPD1s57A1D2Y3vjRhuBmFjT1kVY-FaIN2pR4weifZXEErx_Wn8bxR-cvVOUPiWxH4VfH50_AoygONlYECINL2my3yMRDbNcxZuwOFHLkfTg5DjTd_MnZbKI=235F26E4"

auth = HTTPBasicAuth("adesdorcas@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)

name = output[0]["name"]

print(name)