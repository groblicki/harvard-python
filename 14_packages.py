import sys
import requests
import cowsay

# import json

if len(sys.argv) == 2:
    response = requests.get(
        "https://timeapi.io/api/Time/current/zone?timeZone=Europe/Warsaw"
    )
    cowsay.cow(f"Hello, {sys.argv[1]}!\nIt is {response.json()['time']}")
