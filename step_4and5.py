import requests
host_name = "https://wttr.in/"
parametrs = {"n": "", "T": "", "q": "", "M": "", "lang": "ru"}

geo_locations = ["svo",
                "london", "cherepovets"]

for url in geo_locations:
    response = requests.get(host_name+url, params=parametrs)
    response.raise_for_status()
    print(response.text)
