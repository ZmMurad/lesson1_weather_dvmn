import requests
list1=["http://wttr.dvmn.org/san%20francisco?nTqu&lang=en","http://wttr.dvmn.org/moscow?nTqu&lang=en"]
for url in list1:
  response=requests.get(url)
  response.raise_for_status()
  print(response.text)
  