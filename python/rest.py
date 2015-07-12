

import requests

#test GET session info without authentication
#expect 400
r = requests.get("https://www.browserstack.com/automate/sessions/cd600ca8c745ef30d23e0d27a58d8b99dd0a3416.json")
assert (r.status_code == 401)



#test GET session info with authentication
#expect 200
r = requests.get("https://www.browserstack.com/automate/sessions/cd600ca8c745ef30d23e0d27a58d8b99dd0a3416.json", auth=("shriamin1","LsuuTUS1h1RQ3aNGtZus"))
assert (r.status_code == 200)

