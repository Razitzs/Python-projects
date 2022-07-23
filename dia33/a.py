from urllib import response
import requests

LAT=19.432608
LONG=-99.133209
parameters={
    "lat": LAT,
    "long": LONG,
}

response=requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data=response.json()
# sunrise=data["results"]["sunrise"]
# sunset=data["results"]["sunset"]
print(data)