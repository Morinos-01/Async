import requests

response = requests.get(
    'http://localhost:8080/weather',
    params={'city': 'Los Angeles'}
)

print(response.json())
