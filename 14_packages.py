import sys
import requests
import cowsay
import sayings

# import json

if len(sys.argv) == 2:
    sayings.hello(sys.argv[1])
    response = requests.get(
        "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw"
    )
    cowsay.cow(f"It is {response.json()['time']}")
    sayings.goodbye(sys.argv[1])
