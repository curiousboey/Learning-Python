from urllib import request
import json

url = 'http://official-joke-api.appspot.com/random_ten'
r = request.urlopen(url)
print(r.getcode())
data= r.read()
jsondata= json.loads(data)
print(jsondata)


class joke:
    def __init__(self, setup, punchline) -> None:
        self.setup = setup
        self.punchline = punchline

jokes = []
for j in jsondata:
    setup = j['setup']
    punchline = j['punchline']
    joke =jok
    print()