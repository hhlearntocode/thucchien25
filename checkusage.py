import requests
from config import API_KEY

url = "https://api.thucchien.ai/key/info"

headers = {
  "accept": "application/json",
  "Authorization": f"Bearer {API_KEY}"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    key_info = response.json()
    info = key_info['info']
    print("Key Alias:", info['key_alias'])
    print("Spend: $" + str(info['spend']))
    print("Max Budget:", info.get('max_budget', 'Unlimited'))
    print("Models:", info['models'])
    print("Created:", info['created_at'])
else:
    print("Error:", response.status_code)
    print(response.text)