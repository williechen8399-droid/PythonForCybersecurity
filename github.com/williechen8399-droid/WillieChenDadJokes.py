# Make a joke requesrer 



import urllib.request
import json
# import the function fromr the JSON data
def getDadJoke():
    url = "https://icanhazdadjoke.com/"
    headers = {
        "Accept": "application/json",
        "User-Agent": "WillieDadJokeApp (classproject@.com)"
    }

    request = urllib.request.Request(url, headers=headers)

    with urllib.request.urlopen(request) as response:
        data = response.read().decode("utf-8")

    jokeData = json.loads(data)
    print(jokeData["joke"])

getDadJoke()

