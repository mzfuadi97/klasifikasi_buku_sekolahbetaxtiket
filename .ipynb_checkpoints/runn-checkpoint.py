import requests
import json

headers = {
    'Content-Type': 'application/json;',
}

json_data = json.dumps({
    'inputs': features.tolist()
})

response = requests.post('http://127.0.0.1:8080/invocations', headers=headers, data=json_data)
response.content