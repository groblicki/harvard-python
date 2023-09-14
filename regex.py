import re

name = input("name: ").strip()
email = input("email: ").strip().lower()
url = input("URL: ").strip().lower()

if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

text = f"Hello, {name}"

if matches := re.search(r"^(?:https?://)?(?:www\.)?twitter\.com/([a-z0-9_]+)", url):
    text += f", aka {matches.group(1)}"

text += ". Your email is "

regex = re.compile(
    re.compile(r"([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+")
)
if re.fullmatch(regex, email):
    text += "valid"
else:
    text += "invalid"

text += "."
print(text)
