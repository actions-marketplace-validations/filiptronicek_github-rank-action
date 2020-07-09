import requests, json
from modify import write

country = "czech_republic"
url = f"https://top-ghusers.vercel.app/api?c={country}"

responce = requests.get(url)
resJson = json.loads(responce.text)

for user in resJson['users']:
    if user['user']['username'] == 'filiptronicek':
        write(user['rank'])