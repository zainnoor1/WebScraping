import re
import requests
from bs4 import BeautifulSoup

import re

def matches_company_name(website, names, ignoreCompany):
    website_lower = website.lower()
    url_pattern1 = r"https?://[^/&?]+"
    url_pattern = r"https?://[^/]+"
    url_pattern = r"https?://[^/]+"

    # Check for ignored company names
    for ignore_name in ignoreCompany:
        if ignore_name.lower() in website_lower:
            return False

    # Check for matching names
    for name in names:
        if name.lower() in website_lower:
            match = re.search(url_pattern, website)
            if match:
                basic_url = match.group()
                print(basic_url)
                return True  # Return True if a match is found

    return False  # Return False if no match is found


# Make a request to Google search
company_name="Sarl Cakir"
ignoreCompany=['google','facebook','maps.google','linkedin']
keywords="Albania"
url= "https://www.google.com/search?q="+company_name
url2 = "https://zaynur.pk/"
response = requests.get(url)
website_regex = r'https?://(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]+?\.[a-zA-Z]{2,}(?:\.[a-zA-Z]{2,})?(?:[-a-zA-Z0-9@:%_\+.~#?&//=]*)?'
website_pattern = re.compile(r'https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)')
phone_number_pattern1 = re.compile(r'\+\d{12}')
phone_number_pattern2 = re.compile(r'\+\d{2} \d \d{2} \d{2} \d{2} \d{2}')
phone_number_pattern3 = re.compile(r'\+d{2} \d{3} \d{7}')
phone_number_pattern4 = re.compile(r'\+\d{2}\s\d{3}\s\d{7}')
email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')

# Parse the HTML response
soup = BeautifulSoup(response.content, "html.parser")
a= soup.get_text()
divs = soup.find_all("div")

# Filter divs that contain the company name
filtered_divs = [div for div in divs if company_name.lower() in div.get_text().lower() and "missing" not in div.get_text().lower()]
parent_divs_with_company_name = [div.find_parent("div") for div in divs if company_name.lower() in div.get_text().lower() and "missing" not in div.get_text().lower()]
# Extract data based on phone number patterns
extracted_data = []
website= []
filteredphone_numbers= []
filteredemails= []
# links = soup.find_all("cite")

# company_name1=company_name.replace(" ", "").lower()
# company_name2=company_name.replace(" ", ".").lower()
# company_name3=company_name.replace(" ", "-").lower()
# company_name3=company_name.lower()
# for link in links:
#     linq = text = link.get_text()  
#     website.extend(website_pattern.findall(linq))
words = company_name.split()

# Generate different combinations of words
company_names = []
name_without_spaces = company_name.replace(" ", "")
company_names.append(name_without_spaces)
for i in range(1, len(words) + 1):
    company_names.extend([" ".join(words[j:j+i]) for j in range(len(words) - i + 1)])
for div in filtered_divs:
    if(div!=None):
        text = div.get_text()
        text1=str(div)
        a+=text
        #Step 1 Find Website URLs
        websites = re.findall(website_regex, text1)
        #Step 2 Filter companies url
        filtered_websites = [website for website in websites if matches_company_name(website, company_names,ignoreCompany)]
        for website in filtered_websites:
            print(website)
        filteredphone_numbers.extend(phone_number_pattern1.findall(text))
        filteredphone_numbers.extend(phone_number_pattern2.findall(text))
        filteredphone_numbers.extend(phone_number_pattern3.findall(text))
        filteredphone_numbers.extend(phone_number_pattern4.findall(text))
        filteredemails.extend(email_pattern.findall(text))
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
    
