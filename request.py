import requests

url1 = 'http://localhost:5000/predict_api1'
r1 = requests.post(url1,json={'grade':2, 'square foot of living':9, 'zipcode':6})

print(r1.json())