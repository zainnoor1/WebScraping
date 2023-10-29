import re

url = "https://www.sarlcakir.fr/&amp"

# Define a regular expression pattern to match URLs
url_pattern = r"https?://[^/&?]+"

# Find the URL using the pattern
match = re.search(url_pattern, url)

if match:
    basic_url = match.group()
    print(basic_url)
else:
    print("No URL found in the string.")
