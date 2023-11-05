import requests

x = requests.get('http://localhost:3000').json()

for widget in x:
    print(f"{widget['name']} is {widget['color']}.")

