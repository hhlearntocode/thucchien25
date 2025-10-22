import requests
import json
from config import API_KEY, API_URL

def list_models():
    url = f"{API_URL}/v1/models"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()

def get_model(model_id):
    url = f"{API_URL}/v1/models/{model_id}"
    headers = {"Authorization": f"Bearer {API_KEY}"}
    response = requests.get(url, headers=headers)
    return response.json()

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        result = get_model(sys.argv[1])
    else:
        result = list_models()
    
    if "data" in result:
        print(f"Total models: {len(result['data'])}")
        for model in result['data']:
            print(f"- {model.get('id', 'N/A')}")
    else:
        print(json.dumps(result, indent=2, ensure_ascii=False))

