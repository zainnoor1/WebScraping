import re
import requests
from bs4 import BeautifulSoup

# Make a request to Google search
company_name="zaynur"
keywords="Pakistan Contact Number"
url= "https://www.google.com/search?q="+company_name+keywords
url2 = "https://zaynur.pk/"
response = requests.get(url)
phone_number_pattern1 = re.compile(r'\+\d{12}')
phone_number_pattern2 = re.compile(r'\+\d{2} \d \d{2} \d{2} \d{2} \d{2}')
phone_number_pattern3 = re.compile(r'\+d{2} \d{3} \d{7}')
phone_number_pattern4 = re.compile(r'\+\d{2}\s\d{3}\s\d{7}')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Parse the HTML response
soup = BeautifulSoup(response.content, "html.parser")
divs = soup.find_all("div", class_="BNeawe s3v9rd AP7Wnd")

# Filter divs that contain the company name
filtered_divs = [div for div in divs if company_name.lower() in div.get_text().lower() and "missing" not in div.get_text().lower()]
# Extract data based on phone number patterns
extracted_data = []
filteredphone_numbers= []
filteredemails= []
for div in filtered_divs:
    text = div.get_text()
    filteredphone_numbers.extend(phone_number_pattern1.findall(text))
    filteredphone_numbers.extend(phone_number_pattern2.findall(text))
    filteredphone_numbers.extend(phone_number_pattern3.findall(text))
    filteredphone_numbers.extend(phone_number_pattern4.findall(text))
    filteredemails.extend(email_pattern.findall(text))
# Print the filtered divs
for idx, div in enumerate(filtered_divs, start=1):
    print(f"Div {idx}: {div.get_text(strip=True)}")
    print("----")
for div in divs:
    print(div)
# Regular expression for matching phone numbers in the format +000000000000

# phone_number_pattern2 = re.compile(r'(\+\d{1,3})?[\s.-]?\(?\d{3}\)?[\s.-]?\d{3}[\s.-]?\d{4}')
# Regular expression for matching email addresses
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Extract all text from the HTML
# html_text = soup.get_text()
html_text = str(soup)
# Extract phone numbers from the HTML using the regex pattern
phone_numbers = phone_number_pattern1.findall(html_text)
phone_numbers.extend(phone_number_pattern2.findall(html_text))
phone_numbers.extend(phone_number_pattern3.findall(html_text))
# Extract email addresses from the HTML using the regex pattern
email_addresses = email_pattern.findall(html_text)

# Print the extracted phone numbers and email addresses
if phone_numbers:
    print("Phone Numbers:")
    for phone_number in phone_numbers:
        print(phone_number)
else:
    print("No Phone Number found.")

if email_addresses:
    print("\nEmail Addresses:")
    for email_address in email_addresses:
        print(email_address)
else:
    print("No email addresses found.")
