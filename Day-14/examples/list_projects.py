# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://emenoge-dorcas.atlassian.net/rest/api/3/project"

API_TOKEN = "ATATT3xFfGF0pfDDbb2ZGxAOU94oiyFoH9mHmteuxZpKS1QVYmTQvJJZAhBpgb9dpC_AtsaCewV3vNgi2GBXHyJj_ctfonPygsUVKVlzHv2VcidrW5Z8gUQdDLZYh4BCRN_HAEiQhsQklMq1HgTKQ4mmIF9GMVot2gsUSzI4X4vn4ZamfHyoThw=37285790"
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