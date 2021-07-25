import requests

response = requests.get("https://api.linkedin.com/v2/me")
assert response.status_code == 200
