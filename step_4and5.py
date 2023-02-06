import requests

geolocations=["https://wttr.in/svo?n&m&TMq&lang=ru","https://wttr.in/london?n&m&MTq&lang=ru","https://wttr.in/cherepovets?n&m&MTq&lang=ru"]

for url in geolocations:
  response=requests.get(url)
  response.raise_for_status()
  print(response.text)