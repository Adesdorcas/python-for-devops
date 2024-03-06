# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://emenoge-dorcas.atlassian.net/rest/api/3/issue"

API_TOKEN = "ATATT3xFfGF0pfDDbb2ZGxAOU94oiyFoH9mHmteuxZpKS1QVYmTQvJJZAhBpgb9dpC_AtsaCewV3vNgi2GBXHyJj_ctfonPygsUVKVlzHv2VcidrW5Z8gUQdDLZYh4BCRN_HAEiQhsQklMq1HgTKQ4mmIF9GMVot2gsUSzI4X4vn4ZamfHyoThw=37285790"

auth = HTTPBasicAuth("adesdorcas@gmail.com", API_TOKEN)

headers = {
  "Accept": "application/json",
  "Content-Type": "application/json"
}

payload = json.dumps( {
  "fields": {
    "description": {
      "content": [
        {
          "content": [
            {
              "text": "My first jira ticket",
              "type": "text"
            }
          ],
          "type": "paragraph"
        }
      ],
      "type": "doc",
      "version": 1
    },
    "project": {
      "key": "PYT"
    },
    "issuetype": {
      "id": "10005"
    },
    "summary": "First JIRA Ticket",
  },
  "update": {}
} )

response = requests.request(
   "POST",
   url,
   data=payload,
   headers=headers,
   auth=auth
)

print(json.dumps(json.loads(response.text), sort_keys=True, indent=4, separators=(",", ": ")))