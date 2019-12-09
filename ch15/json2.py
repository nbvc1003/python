import requests, json
import pandas as pd

url = 'https://api.github.com/repositories'
data = requests.get(url)
print(data.text)
result = json.loads(data.text)

df = pd.DataFrame(result, columns=['name','full_name'])
print(df)