import sys
import requests
import cowsay
import lib_sayings

# import json

if len(sys.argv) == 2:
    lib_sayings.hello(sys.argv[1])
    response = requests.get(
        "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw"
    )
    cowsay.cow(f"It is {response.json()['time']}")
    lib_sayings.goodbye(sys.argv[1])
